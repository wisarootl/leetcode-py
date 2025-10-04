PYTHON_VERSION = 3.13
PROBLEM ?= same_tree
FORCE ?= 0
COMMA := ,

sync_submodules:
	git submodule update --init --recursive --remote

# WARNING: Opinionated development setup for macOS + zsh + brew
# This will install/update many tools: pipx, poetry, pre-commit, etc.
# Only use if you understand what it does and accept the changes
setup_dev: sync_submodules
	chmod +x scripts/shared/python/poetry/setup_dev.sh
	./scripts/shared/python/poetry/setup_dev.sh \
		--python-version $(PYTHON_VERSION) \
		--colima-docker
	exec /usr/bin/env zsh

assert_setup_dev:
	chmod +x scripts/shared/python/poetry/assert_setup_dev.sh
	./scripts/shared/python/poetry/assert_setup_dev.sh

define lint_target
	poetry run black $(1)
	poetry run isort $(1)
	$(if $(filter .,$(1)), \
		poetry run nbqa ruff . --nbqa-exclude="leetcode_py/cli/resources/" --ignore=F401$(COMMA)F821, \
		poetry run nbqa ruff $(1) --ignore=F401$(COMMA)F821)
	poetry run ruff check $(1) --exclude="**/*.ipynb"
	poetry run mypy $(1) \
		--explicit-package-bases \
		--install-types \
		--non-interactive \
		--check-untyped-defs
	$(if $(filter .,$(1)), \
		poetry run nbqa isort . --nbqa-exclude="leetcode_py/cli/resources/", \
		poetry run nbqa isort $(1))
	$(if $(filter .,$(1)), \
		poetry run nbqa mypy . --nbqa-exclude="leetcode_py/cli/resources/" \
			--ignore-missing-imports --disable-error-code=name-defined, \
		poetry run nbqa mypy $(1) --ignore-missing-imports --disable-error-code=name-defined)
endef

lint:
	poetry run python scripts/sort_tags.py
	poetry run python scripts/check_tag_problems.py
	poetry sort
	npx prettier --write "**/*.{ts,tsx,css,json,yaml,yml,md}"
	$(call lint_target,.)

test:
	poetry run pytest leetcode/ tests/ \
		-v --cov=leetcode --cov=leetcode_py \
		--cov-report=term-missing \
		--cov-report=xml \
		--ignore=.templates \
		--ignore=leetcode/__pycache__

p-test:
	@echo "Testing problem: $(PROBLEM)"
	@if [ ! -d "leetcode/$(PROBLEM)" ]; then \
		echo "Error: Problem '$(PROBLEM)' not found in leetcode/ directory"; \
		exit 1; \
	fi
	poetry run pytest leetcode/$(PROBLEM)/test_solution.py -v -s

p-lint:
	@echo "Linting problem: $(PROBLEM)"
	@if [ ! -d "leetcode/$(PROBLEM)" ]; then \
		echo "Error: Problem '$(PROBLEM)' not found in leetcode/ directory"; \
		exit 1; \
	fi
	$(call lint_target,leetcode/$(PROBLEM))

p-gen:
	@echo "Generating problem: $(PROBLEM)"
	poetry run lcpy gen -s $(PROBLEM) -o leetcode $(if $(filter 1,$(FORCE)),--force)

p-del:
	rm -rf leetcode/$(PROBLEM)

# Convert all notebooks to .py files and delete .ipynb for better version control
nb-to-py:
	@echo "Converting all .ipynb files in leetcode/ to .py files..."
	@find leetcode -name "*.ipynb" -exec poetry run jupytext --to py:percent {} \;
	@find leetcode -name "*.ipynb" -delete
	@echo "Conversion complete. All .ipynb files converted to .py and deleted."

# Find problems with few test cases
check-test-cases:
	@echo "Checking test case coverage..."
	poetry run python leetcode_py/tools/check_test_cases.py --threshold=$(or $(THRESHOLD),10) --max=$(or $(MAX),1)

# Generate All Problems - useful for people who fork this repo
gen-all-problems:
	@echo "This will DELETE all existing problems and regenerate from JSON templates."
	@if [ "$$CI" != "true" ]; then \
		read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1; \
	fi
	@echo "Deleting existing problems..."
	@rm -rf leetcode/*/
	@echo "Generating all problems..."
	poetry run lcpy gen --all -o leetcode $(if $(filter 1,$(FORCE)),--force)

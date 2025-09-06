PYTHON_VERSION = 3.13
PROBLEM ?= basic_calculator
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
		poetry run nbqa ruff . --nbqa-exclude=".templates" --ignore=F401$(COMMA)F821, \
		poetry run nbqa ruff $(1) --ignore=F401$(COMMA)F821)
	poetry run ruff check $(1) --exclude="**/*.ipynb"
	poetry run mypy $(1) \
		--explicit-package-bases \
		--install-types \
		--non-interactive \
		--check-untyped-defs
	$(if $(filter .,$(1)), \
		poetry run nbqa isort . --nbqa-exclude=".templates", \
		poetry run nbqa isort $(1))
	$(if $(filter .,$(1)), \
		poetry run nbqa mypy . --nbqa-exclude=".templates" \
			--ignore-missing-imports --disable-error-code=name-defined, \
		poetry run nbqa mypy $(1) --ignore-missing-imports --disable-error-code=name-defined)
endef

lint:
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
	poetry run pytest leetcode/$(PROBLEM)/tests.py -v -s

p-lint:
	@echo "Linting problem: $(PROBLEM)"
	@if [ ! -d "leetcode/$(PROBLEM)" ]; then \
		echo "Error: Problem '$(PROBLEM)' not found in leetcode/ directory"; \
		exit 1; \
	fi
	$(call lint_target,leetcode/$(PROBLEM))

p-gen:
	@echo "Generating problem: $(PROBLEM)"
	poetry run python .templates/leetcode/gen.py .templates/leetcode/json/$(PROBLEM).json $(if $(filter 1,$(FORCE)),--force)

p-del:
	rm -rf leetcode/$(PROBLEM)

# Generate All Problems - useful for people who fork this repo
gen-all-problems:
	@echo "This will DELETE all existing problems and regenerate from JSON templates."
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@echo "Deleting existing problems..."
	@rm -rf leetcode/*/
	@echo "Generating all problems..."
	@for json_file in .templates/leetcode/json/*.json; do \
		problem=$$(basename "$$json_file" .json); \
		echo "Generating: $$problem"; \
		poetry run python .templates/leetcode/gen.py "$$json_file" $(if $(filter 1,$(FORCE)),--force); \
	done

PYTHON_VERSION = 3.13
QUESTION ?= insert_interval
FORCE ?= 0

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

lint:
	poetry sort
	npx prettier --write "**/*.{ts,tsx,css,json,yaml,yml,md}"
	poetry run black .
	poetry run isort .
	poetry run nbqa ruff . --nbqa-exclude=".templates" --ignore=F401,F821
	poetry run ruff check . --exclude="**/*.ipynb"
	poetry run mypy \
		--explicit-package-bases \
		--install-types \
		--non-interactive \
		--check-untyped-defs .
	poetry run nbqa isort . --nbqa-exclude=".templates"
	poetry run nbqa mypy . \
		--nbqa-exclude=".templates" \
		--ignore-missing-imports \
		--disable-error-code=name-defined


test:
	poetry run pytest leetcode/ \
		-v --cov=leetcode --cov=leetcode_py \
		--cov-report=term-missing \
		--cov-report=xml \
		--ignore=.templates \
		--ignore=leetcode/__pycache__

# Test Questions
q-test:
	@echo "Testing question: $(QUESTION)"
	@if [ ! -d "leetcode/$(QUESTION)" ]; then \
		echo "Error: Question '$(QUESTION)' not found in leetcode/ directory"; \
		exit 1; \
	fi
	poetry run pytest leetcode/$(QUESTION)/tests.py -v -s

# Generate Question
q-gen:
	@echo "Generating question: $(QUESTION)"
	poetry run python .templates/leetcode/gen.py .templates/leetcode/json/$(QUESTION).json $(if $(filter 1,$(FORCE)),--force)

# Generate All Questions - useful for people who fork this repo
gen-all-questions:
	@echo "This will DELETE all existing questions and regenerate from JSON templates."
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@echo "Deleting existing questions..."
	@rm -rf leetcode/*/
	@echo "Generating all questions..."
	@for json_file in .templates/leetcode/json/*.json; do \
		question=$$(basename "$$json_file" .json); \
		echo "Generating: $$question"; \
		poetry run python .templates/leetcode/gen.py "$$json_file" $(if $(filter 1,$(FORCE)),--force); \
	done

# Validate Question - INTERNAL USE ONLY: For cookiecutter template creation/validation
# Do not use during normal problem solving - only for template development
q-validate:
	@echo "Validating question: $(QUESTION)"
	@if [ ! -d "leetcode/$(QUESTION)" ]; then \
		echo "Error: Generated question '$(QUESTION)' not found. Run: make q-gen QUESTION=$(QUESTION)"; \
		exit 1; \
	fi
	poetry run python .amazonq/plan/compare_template_files.py generated --question=$(QUESTION)

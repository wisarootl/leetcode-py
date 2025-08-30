PYTHON_VERSION = 3.13
QUESTION ?= invert_binary_tree

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
	poetry run black .
	poetry run isort .
	poetry run ruff check .
	poetry run mypy \
		--explicit-package-bases \
		--install-types \
		--non-interactive \
		--check-untyped-defs .
	npx prettier --write "**/*.{ts,tsx,css,json,yaml,yml,md}"


test:
	poetry run pytest leetcode/ \
		-v --cov=leetcode --cov=leetcode_py \
		--cov-report=term-missing \
		--cov-report=xml \
		--ignore=leetcode/_template \
		--ignore=leetcode/__pycache__

test-question:
	@echo "Testing question: $(QUESTION)"
	@if [ ! -d "leetcode/$(QUESTION)" ]; then \
		echo "Error: Question '$(QUESTION)' not found in leetcode/ directory"; \
		exit 1; \
	fi
	poetry run pytest leetcode/$(QUESTION)/tests.py -v -s

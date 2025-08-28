PYTHON_VERSION = 3.13
QUESTION ?= two_sum

sync_submodules:
	git submodule update --init --recursive --remote

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
		--ignore=leetcode/_template \
		--ignore=leetcode/__pycache__

test-question:
	@echo "Testing question: $(QUESTION)"
	@if [ ! -d "leetcode/$(QUESTION)" ]; then \
		echo "Error: Question '$(QUESTION)' not found in leetcode/ directory"; \
		exit 1; \
	fi
	cd leetcode/$(QUESTION) && poetry run pytest tests.py -v -s

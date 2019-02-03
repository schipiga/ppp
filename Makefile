.DEFAULT_GOAL := help
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install project dependencies. Make sure you have installed globally `python3`, `pip`, `virtualenv`.
	echo "Installing virtual environment..."
	test -d .venv || virtualenv .venv -p python3.7
	echo "Installing python requirements..."
	./.venv/bin/pip install -r dev-requirements.txt
	echo "Installing git hooks..."
	./.venv/bin/pre-commit install
	echo "All done! Enjoy ;)"

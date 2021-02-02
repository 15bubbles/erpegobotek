
# INSTALLATION TARGETS
install:
	pip install poetry
	poetry install


# BOT RUNNING TARGETS
local-run-discord:
	poetry run python erpegobotek\bot\discord

local-run: local-run-discord

run-discord:
	echo "Implement me"

run: run-discord


# DEVELOPMENT TOOLS' TARGETS, STATIC CODE ANALYSIS, LINTING, FORMATTING
lint:
	poetry run pylint $(APP_MODULE)

flake:
	poetry run flake8 $(APP_MODULE) --max-line-length=100

sort-imports:
	poetry run isort $(APP_MODULE)

remove-unused-imports:
	poetry run autoflake --remove-all-unused-imports $(APP_MODULE)

type-check:
	poetry run mypy $(APP_MODULE)

format: remove-unused-imports
	poetry run black $(APP_MODULE)


# TEST RUNNING TARGETS
local-coverage:
	echo "Implement me"

local-test-unit:
	echo "Implement me"

local-test: local-test-unit

test-unit:
	echo "Implement me"

test: test-unit

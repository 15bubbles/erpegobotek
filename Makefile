APP_MODULE = erpegobotek


# INSTALLATION TARGETS
install:
	pip install poetry
	poetry install


# BOT RUNNING TARGETS
local-run-discord:
	poetry run python $(APP_MODULE)/bot/discord

local-run: local-run-discord

build-discord:
	docker-compose -f docker/docker-compose.yaml build

run-discord:
	docker-compose -f docker/docker-compose.yaml up

run: build-discord run-discord


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
local-test: local-test-unit

test-build:
	docker-compose -f docker/docker-compose.yaml -f docker/docker-compose.test.yaml build

test-run:
	docker-compose -f docker/docker-compose.yaml -f docker/docker-compose.test.yaml up

test: test-build test-run

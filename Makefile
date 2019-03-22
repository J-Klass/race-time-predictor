MAKEFLAGS += -j2
MODULE_PATH = race_time_predictor

.PHONY: install
install:
	git config core.hooksPath .hooks
	pipenv install --dev
	yarn install

.PHONY: start
start: start_python start_js

.PHONY: start_python
start_python:
	export FLASK_ENV=development; pipenv run python run.py

.PHONY: start_js
start_js:
	yarn start

.PHONY: build
build:
	yarn build

.PHONY: format
format:
	pipenv run black ${MODULE_PATH} --line-length=100 $(BLACK_FLAGS)

.PHONY: lint
lint:
	pipenv run flake8 ${MODULE_PATH} --max-line-length=100
	yarn lint

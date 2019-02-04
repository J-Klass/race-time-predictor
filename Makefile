MAKEFLAGS += -j2

.PHONY: install
install:
	pipenv install --dev
	yarn install

.PHONY: hooks
hooks:
	git config core.hooksPath .hooks

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
	black race_time_predictor --line-length=100 $(BLACK_FLAGS)

.PHONY: lint
lint:
	flake8 race_time_predictor --max-line-length=100
	yarn lint

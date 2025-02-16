.PHONY: install \
	run-backend run-frontend \
	unit-tests integration-tests e2e-tests e2e-tests-headless \
	tests tests-headless



install:
	poetry env use 3.13
	poetry install
	poetry run playwright install --with-deps chromium
	cd frontend && npm install

start-backend:
	poetry run python -m backend.main

start-frontend:
	cd frontend && npm run dev



unit-tests:
	poetry run pytest -sv tests/unit

integration-tests:
	poetry run pytest -sv tests/integration

e2e-tests:
	PWDEBUG=console poetry run pytest -sv tests/e2e

e2e-tests-headless:
	poetry run pytest -sv tests/e2e

tests: unit-tests integration-tests e2e-tests

tests-headless: unit-tests integration-tests e2e-tests-headless

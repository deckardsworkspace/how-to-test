how-to-test
=========

This is a very basic sample project to demonstrate how to test a web app via unit tests, integration tests, and end-to-end (E2E) tests.

The web app is a simple application that allows the user to read and write to a "database" (implemented as a text file) on a remote server.

The backend is written in Python using [FastAPI](https://fastapi.tiangolo.com/), and the frontend is written in [Vue 3](https://vuejs.org/). The tests are ran using [pytest](https://docs.pytest.org/en/stable/), and the E2E tests make use of [Playwright](https://playwright.dev/) to automate the browser.

## Installation

Ensure you have GNU Make, Python 3.13+, and Node.js + npm installed.

To install the project dependencies, run

```
make install
```

## Starting the app

You will need to start two terminal instances, one for the frontend and another for the backend.

To start the backend, run

```
make start-backend
```

in the first terminal instance. To start the frontend, run

```
make start-frontend
```

in the second terminal instance.

You can access the backend at `http://localhost:12345` and the frontend at `http://localhost:5173`.

**Important:** The app will need to be running before you can run integration and E2E tests.

## Running tests

To run all tests, run `make tests`.

To run one class of tests only, use

- `make unit-tests` to run unit tests
- `make integration-tests` to run integration tests
- `make e2e-tests` to run E2E tests

**Tip:** You can tell Playwright to pause at any time during the test by adding `page.pause()` to your test case. See `test_text.py` for example usage.

### Headless mode

The above commands will run E2E tests in *headed* mode, which is where you can see the browser on your screen when your app is being tested. This is so you can follow along and see what Playwright is doing.

To run E2E tests in *headless* mode, run `make e2e-tests-headless` (or `make tests-headless` to run all tests in headless mode).

### Limitations

The unit tests only cover the backend. There are no unit tests yet for the frontend, but part of it is covered by the E2E tests.

The project has been bootstrapped with support for [Vitest](https://vitest.dev/), so unit tests for the frontend can be added easily in the future.

## License

```
Copyright 2025 Aurel Jared C. Dantis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

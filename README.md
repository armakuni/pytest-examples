# Pytest examples

This repository contains examples for real-world pytest use cases. It is intended as a "cheatsheet" of working examples that you can pick and choose to meet your particular need.

Resources we really encourage you to learn:

| Resource                                                                                | Description                                                                                                                                               |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Pytest home page](https://docs.pytest.org/en/6.2.x/index.html)                         | The primary resource for pytest knowledge.                                                                                                                |
| [Core mocking framework](https://docs.python.org/3/library/unittest.mock.html)          | This is Python's built-in unittest/mocking framework. It's not easy to read.                                                                              |
| [Responses framework](https://docs.python-requests.org/en/latest/user/quickstart/)      | This is a comprehensive mocking framework for HTTP requests. Use it when you want to test a request to a third-party API.                                 |
| [Moto AWS mocking library](http://docs.getmoto.org/en/latest/docs/getting_started.html) | This is a relatively fully featured mocking framework for boto3. It holds AWS resource state in memory, which is especially useful for behavioural tests. |

## Installation and running

```sh
pip3 install -r requirements.txt
pytest -v
```

## Layout

All of the test examples live in the [tests](tests) folder:

| Subfolder                  | Description                                                                               |
|----------------------------|-------------------------------------------------------------------------------------------|
| [aws](tests/aws)           | Shows how to mock AWS calls.                                                              |
| [fixtures](tests/fixtures) | Examples for using pytest fixtures.                                                       |
| [http](tests/http)         | Shows how to mock HTTP calls - to third party APIs, for example.                          |
| [mocking](tests/mocking)   | Examples demonstrating how to mock functions, class methods, etc.                         |
| [simple](tests/simple)     | Demonstrations of common pytest use cases, such as asserting that an exception is thrown. |

Some of the test examples explore classic import gotchas. The source code that is tested resides in [lib](lib).

## Fizzbuzz application

We created a simple "application", [fizzbuzz](fizzbuzz) to show many of the testing techniques in action. This application consists of a web server (wrapping a library method in an API) and a client. It demonstrates how you would unit test each part in isolation - so, for example, you would do not run the server to validate the client.

You can find the tests in [tests/fizzbuzz](tests/fizzbuzz).
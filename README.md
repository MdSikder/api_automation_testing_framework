# API Automation Testing Framework

## Overview
`api-automation-testing-framework` is a comprehensive framework designed for automating API testing. It utilizes `pytest` for writing and running tests, with integrated logging and configuration management.

## Features
- **Automated Testing**: Easily create and run automated tests for your APIs.
- **Logging**: Integrated logging to capture detailed test run information.
- **Configuration Management**: Centralized configuration management for easy setup and maintenance.
- **Extensible**: Easily extend and customize for different API testing needs.

## Getting Started

### Prerequisites
- Python 3.x
- `pytest`
- `requests`
- `pytest-html` (for HTML reports)
- `pytest-cov` (for coverage reports)

Install the required packages:
```bash
pip install -r requirements.txt

Running Tests
Run all tests and generate an HTML report and coverage report:
        bash run_tests.sh



### Directory Structure:

        api-automation-testing-framework/
        │
        ├── configurations/
        │   └── config.ini
        ├── logs/
        │   └── test_logs.log
        ├── src/
        │   ├── __init__.py
        │   ├── api_client.py
        │   └── config_parser.py
        ├── tests/
        │   ├── integration_tests/
        │   │   ├── __init__.py
        │   │   ├── test_generate_token.py
        │   │   ├── test_new_booking.py
        │   │   └── test_update.py
        │   ├── __init__.py
        │   └── conftest.py
        ├── .gitignore
        ├── README.md
        ├── run_tests.sh
        ├── pytest.ini
        └── requirements.txt

configurations/: Configuration files.
logs/: Log files generated during test runs.
src/: Source files including API client and configuration parser.
tests/: Test cases and fixtures.


### Contributing
Contributions are welcome! Please submit a pull request or create an issue for any changes or suggestions.

License
This project is licensed under the MIT License.


### `run_tests.sh` Example
```bash
#!/bin/bash

# Create reports directory if it doesn't exist
mkdir -p reports

# Run tests with HTML and coverage report
pytest --html=reports/test_report.html --cov=src --cov-report=html:reports/coverage_report

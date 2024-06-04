import pytest
import logging
import os


# Configure the logging for pytest
def pytest_configure(config):
    # Ensure logs directory exists
    logs_dir = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(logs_dir, "test_logs.log"),  # Corrected path
        level=logging.INFO,  # Log level
        format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
    )

    # Force flush at end of each test session
    config.add_cleanup(logging.shutdown)


@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"

import logging
import requests
import pytest
from src.config_parser import ReadConfig

# Get the logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Body for authentication
body = {
    "username": "admin",
    "password": "password123"
}


def get_auth_token():
    base_url = ReadConfig.get_base_url()
    logger.info("Entering get_auth_token")
    # Endpoint for creating a token
    auth_url = f"{base_url}/auth"

    # Make a POST request to the /auth endpoint
    response = requests.post(f"{base_url}/auth", json=body)
    # Raise an error if the request was unsuccessful
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Return the token
    return data['token']


def test_get_auth_token():
    # Get the token using the function
    token = get_auth_token()

    # Print the token
    logger.info(f"Token: {token}")

    print(f"Token: {token}")

    # Assert that the token is not empty
    assert token


if __name__ == "__main__":
    pytest.main(["-s", "test_api_endpoints.py"])

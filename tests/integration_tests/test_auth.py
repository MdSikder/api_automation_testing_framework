import logging
import requests
import pytest

# Get the logger
logger = logging.getLogger(__name__)

# body for authentication
body = {
    "username": "admin",
    "password": "password123"
}


def get_auth_token(base_url):
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


def test_get_auth_token(base_url):
    # Get the token using the function
    token = get_auth_token(base_url)

    # Print the token
    logger.info(f"Token: {token}")

    print(f"Token: {token}")

    # Assert that the token is not empty
    assert token


if __name__ == "__main__":
    pytest.main(["-s", "test_auth.py"])

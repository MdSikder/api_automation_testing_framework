import logging
import requests
import pytest
import json
from src.config_parser import ReadConfig

# Get the logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Base URL from config files
BASE_URL = ReadConfig.get_base_url()

# Booking data for creation
body = {
    "firstname": "Sally",
    "lastname": "Brown-5",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2013-02-23",
        "checkout": "2014-10-23"
    },
    "additionalneeds": "Breakfast"
}

# Updated booking data for PUT request
updated_body = {
    "firstname": "John",
    "lastname": "Doe-Updated",
    "totalprice": 150,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2013-03-01",
        "checkout": "2014-11-01"
    },
    "additionalneeds": "Lunch"
}


def create_booking():
    # Endpoint for creating a booking
    booking_url = f"{BASE_URL}/booking"

    # Headers for the request
    headers = {
        "Content-Type": "application/json"
    }

    # Make a POST request to the /booking endpoint
    response = requests.post(booking_url, headers=headers, json=body)

    # Raise an error if the request was unsuccessful
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Return the booking ID
    return data['bookingid']


def get_booking(booking_id):
    # Endpoint for retrieving a booking
    booking_url = f"{BASE_URL}/booking/{booking_id}"

    # Make a GET request to the /booking/{id} endpoint
    response = requests.get(booking_url)

    # Raise an error if the request was unsuccessful
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Return the response data
    return data


def update_booking(booking_id, update_body):
    # Endpoint for updating a booking
    booking_url = f"{BASE_URL}/booking/{booking_id}"

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "token=fd533a638f39a64"  # Validate this token
    }

    # Make a PUT request to the /booking/{id} endpoint
    response = requests.put(booking_url, headers=headers, json=update_body)

    # Raise an error if the request was unsuccessful
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Return the response data
    return data


def test_put_booking():
    # Create a booking and get the booking ID
    booking_id = create_booking()

    # Update the booking using the booking ID
    updated_response_data = update_booking(booking_id, updated_body)

    logger.info(f"\nUpdated id: {booking_id}")
    # Print the response data
    logger.info(f"\n{json.dumps(updated_response_data, indent=4)}")

    # Assert that the response contains the updated data
    assert updated_response_data['firstname'] == updated_body['firstname']
    assert updated_response_data['lastname'] == updated_body['lastname']
    assert updated_response_data['totalprice'] == updated_body['totalprice']
    assert updated_response_data['depositpaid'] == updated_body['depositpaid']
    assert updated_response_data['bookingdates']['checkin'] == updated_body['bookingdates']['checkin']
    assert updated_response_data['bookingdates']['checkout'] == updated_body['bookingdates']['checkout']
    assert updated_response_data['additionalneeds'] == updated_body['additionalneeds']


if __name__ == "__main__":
    pytest.main(["-s", "test_put_request.py"])

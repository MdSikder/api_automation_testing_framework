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


def create_booking():
    # Endpoint for creating a booking
    booking_url = f"{BASE_URL}/booking"

    # Headers for the request
    headers = ReadConfig.get_header_content_type()

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


def test_get_booking():
    # Create a booking and get the booking ID
    booking_id = create_booking()

    # Retrieve the booking using the booking ID
    response_data = get_booking(booking_id)

    logger.info(f"\nid: {booking_id}")
    # Print the response data
    logger.info(f"\n{json.dumps(response_data, indent=4)}")

    # Assert that the response contains the expected data
    assert response_data['firstname'] == body['firstname']
    assert response_data['lastname'] == body['lastname']
    assert response_data['totalprice'] == body['totalprice']
    assert response_data['depositpaid'] == body['depositpaid']
    assert response_data['bookingdates']['checkin'] == body['bookingdates']['checkin']
    assert response_data['bookingdates']['checkout'] == body['bookingdates']['checkout']
    assert response_data['additionalneeds'] == body['additionalneeds']


if __name__ == "__main__":
    pytest.main(["-s", "test_get_booking.py"])

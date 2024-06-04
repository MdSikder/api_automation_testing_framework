def assert_api_response(response, expected_status):
    assert response["status"] == expected_status, f"Expected {expected_status}, got {response['status']}"

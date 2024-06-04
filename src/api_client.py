import requests


class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}{endpoint}", json=data, headers=self.headers)
        return response.json()

    # Add more methods for PUT, DELETE, etc.

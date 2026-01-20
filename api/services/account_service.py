import requests
from api.config import BASE_URL

class AccountService:

    def create_user(self, username, password):
        return requests.post(
            f"{BASE_URL}/Account/v1/User",
            json={"userName": username, "password": password}
        )

    def generate_token(self, username, password):
        return requests.post(
            f"{BASE_URL}/Account/v1/GenerateToken",
            json={"userName": username, "password": password}
        )

    def authorized(self, username, password):
        return requests.post(
            f"{BASE_URL}/Account/v1/Authorized",
            json={"userName": username, "password": password}
        )

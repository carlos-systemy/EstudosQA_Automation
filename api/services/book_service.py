import requests
from api.config import BASE_URL

class BookService:

    def list_books(self):
        return requests.get(f"{BASE_URL}/BookStore/v1/Books")

    def rent_books(self, token, user_id, books):
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"userId": user_id, "collectionOfIsbns": books}

        return requests.post(
            f"{BASE_URL}/BookStore/v1/Books",
            headers=headers,
            json=payload
        )

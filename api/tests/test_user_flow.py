from api.services.account_service import AccountService
from api.services.book_service import BookService
from api.config import USERNAME, PASSWORD

def test_user_flow():
    account = AccountService()
    book = BookService()

    create = account.create_user(USERNAME, PASSWORD)
    assert create.status_code in [201, 406]

    if create.status_code == 201:
        user_id = create.json()["userID"]
    else:
        user_id = None

    token_resp = account.generate_token(USERNAME, PASSWORD)
    assert token_resp.status_code == 200
    token = token_resp.json()["token"]

    auth = account.authorized(USERNAME, PASSWORD)
    assert auth.status_code == 200
    assert auth.json() is True

    books = book.list_books().json()["books"][:2]
    isbns = [{"isbn": b["isbn"]} for b in books]

    rent = book.rent_books(token, user_id, isbns)
    assert rent.status_code == 201

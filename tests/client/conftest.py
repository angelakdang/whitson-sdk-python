import json

import pytest

from whitson.client.config import Token


@pytest.fixture()
def token():
    token = Token(
        access_token="abcdefghijklmnopqrstuvwxyz",
        scope="get:api post:api delete:api",
        issued_at=4102444800.0,  # Friday, January 1, 2100 12:00:00 AM
        expires_in=86400,  # 24 hours
        token_type="Bearer",
    )
    yield token


@pytest.fixture()
def token_path():
    token = {
        "access_token": "abcdefghijklmnopqrstuvwxyz",
        "scope": "get:api post:api delete:api",
        "issued_at": 4102444800.0,  # Friday, January 1, 2100 12:00:00 AM
        "expires_in": 86400,  # 24 hours
        "token_type": "Bearer",
    }
    yield json.dumps(token, indent=4)

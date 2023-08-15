import pytest
import logging
from whitson.client.config import Token, ClientConfig

logger = logging.getLogger(__name__)


class TestToken(object):
    def test_correct_data_types(self, token):
        assert token.access_token == "abcdefghijklmnopqrstuvwxyz"
        assert token.scope == "get:api post:api delete:api"
        assert token.issued_at == 4102444800.0
        assert token.expires_in == 86400
        assert token.token_type == "Bearer"

    def test_incorrect_data_type(self):
        with pytest.raises(ValueError, match="issued_at is an incorrect data type."):
            Token(
                access_token="abcdefghijklmnopqrstuvwxyz",
                scope="get:api post:api delete:api",
                issued_at="4102444800",  # should be float type
                expires_in=86400,
                token_type="Bearer"
            )

    def test_expired_token(self, caplog):
        token = Token(
            access_token="abcdefghijklmnopqrstuvwxyz",
            scope="get:api post:api delete:api",
            issued_at=1691971200.0,  # Monday, August 14, 2023 12:00:00 AM
            expires_in=86400,  # 24 hours
            token_type="Bearer"
        )
        assert "Specified Token is expired." in caplog.text


class TestClientConfig(object):
    def test_token_specified(self, token):
        config = ClientConfig(token=token, client_name="client_name")
        assert config.token.access_token == "abcdefghijklmnopqrstuvwxyz"

    def test_no_client_name(self):
        with pytest.raises(ValueError, match="No client name specified."):
            ClientConfig(token=None, client_name=None, client_id="client_id", client_secret="client_secret")

    def test_no_client_id(self):
        with pytest.raises(ValueError, match="No client id specified."):
            ClientConfig(token=None, client_name="client_name", client_id=None, client_secret="client_secret")

    def test_no_client_secret(self):
        with pytest.raises(ValueError, match="No client secret specified."):
            ClientConfig(token=None, client_name="client_name", client_id="client_id", client_secret=None)

import logging

import pytest

from whitson.client.config import ClientConfig, Token

logger = logging.getLogger(__name__)


class TestToken:
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
                token_type="Bearer",
            )

    def test_expired_token(self, caplog):
        Token(
            access_token="abcdefghijklmnopqrstuvwxyz",
            scope="get:api post:api delete:api",
            issued_at=1691971200.0,  # Monday, August 14, 2023 12:00:00 AM
            expires_in=86400,  # 24 hours
            token_type="Bearer",
        )
        assert "Specified Token is expired." in caplog.text


class TestClientConfig:
    def test_token_specified(self, token):
        config = ClientConfig(client_name="client_name", token_path="token.json")
        assert config.token.access_token == "abcdefghijklmnopqrstuvwxyz"

    def test_no_client_name(self):
        with pytest.raises(ValueError, match="No client name specified."):
            ClientConfig(
                client_name=None,
                token_path="token.json",
            )

    def test_no_client_id(self):
        """Wrong token path requires ClientConfig to generate new token, requiring client_id AND client_secret."""
        with pytest.raises(ValueError, match="No client id specified."):
            ClientConfig(
                client_name="client_name",
                token_path="wrong_token_path.json",
                client_id=None,
                client_secret="client_secret",
            )

    def test_no_client_secret(self):
        """Wrong token path requires ClientConfig to generate new token, requiring client_id AND client_secret."""
        with pytest.raises(ValueError, match="No client secret specified."):
            ClientConfig(
                client_name="client_name",
                token_path="wrong_token_path.json",
                client_id="client_id",
                client_secret=None,
            )

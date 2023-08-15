import os
import time
import logging
import requests
from dacite import from_dict


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)


class Token:
    """Defines the Token object to be passed into the ClientConfig if it exists.

    Parameters
    ----------
    access_token :
        param scope: scope of the Token, typically "get:api post:api delete:api"
    issued_at :
        UTC timestamp of when the token was issued
    expires_in :
        time in seconds of how long the token is issued for
    token_type :
        typically "Bearer"
    """

    def __init__(
            self,
            access_token: str,
            scope: str,
            issued_at: float,
            expires_in: int,
            token_type: str
    ):
        self.access_token = access_token
        self.scope = scope
        self.issued_at = issued_at
        self.expires_in = expires_in
        self.token_type = token_type


class ClientConfig:
    """Configuration object to instantiate the WhitsonClient

    client_id and client_secret must be specified if Token is not specified.

    Parameters
    ----------
    token : Token
        Token
    client_name : str
        client name, defined by Whitson
    client_id : str, optional
        client id, obtained from Whitson (Default value = None)
    client_secret : str, optional
        client secret obtained from Whitson (Default value = None)
    pem_path : str, optional
        path to PEM file containing required security certificates (Default value = None)
    """
    def __init__(
        self,
        token: Token | None,
        client_name: str,
        client_id: str = None,
        client_secret: str = None,
        pem_path: str = None,
    ):
        self.client_name = client_name

        # Determine if token is expired
        is_not_expired = True if time.time() < (token.issued_at + token.expires_in) else False

        if token and is_not_expired:
            self.token = token
            logger.info(f"Access token specified.")
        else:
            # Check to see if required params for obtaining Token are present
            if not client_id:
                raise ValueError("No client id specified.")
            if not client_secret:
                raise ValueError("No client secret specified.")
            self.client_id = client_id
            self.pem_path = pem_path

            # Point to a PEM file containing required security certificates
            os.environ['REQUESTS_CA_BUNDLE'] = pem_path

            url = f"https://whitson.eu.auth0.com/oauth/token"
            payload = {
                "client_id": client_id,
                "client_secret": client_secret,
                "audience": f"https://{client_name}.whitson.com/",
                "grant_type": "client_credentials",
            }
            headers = {"content-type": "application/json"}
            issued_at = time.time()
            res = requests.post(url, json=payload, headers=headers)
            data = res.json()
            data["issued_at"] = issued_at

            self.token = from_dict(data=data, data_class=Token)
            logger.info(f"New token retrieved: {data}")

import requests

from whitson.client.config import ClientConfig


class WhitsonClient:
    """Main entrypoint into the Whitson Python SDK to access data from Whitson+

    Parameters
    ----------
    config: ClientConfig
        Configuration objection for WhitsonClient
    """

    def __init__(self, config: ClientConfig):
        if config is None:
            raise ValueError("No ClientConfig has been provided.")
        else:
            self.config = config
            self.base_url = f"http://{config.client_name}.whitson.com/api-external/v1/"

    def get(self, suffix: str, params: dict) -> dict:
        """Perform a GET request to an arbitrary path in the API.

        Parameters
        ----------
        suffix : str
            Suffix to add to the base url for API request
        params : dict
            Dictionary of parameters for the request

        Returns
        -------
        res : dict
        """
        response = requests.get(
            url=self.base_url + suffix,
            headers={
                "content_type": "application/json",
                "Authorization": f"Bearer {self.config.token.access_token}",
            },
            params=params,
        )
        res = response.json()
        if not res:
            raise Exception("No information retrieved")
        return res

    def post(self, suffix: str, payload: dict):
        """Perform a POST request to an arbitrary path in the API.

        Parameters
        ----------
        suffix : str
            Suffix to add to the base url for API request
        payload : dict
            Dictionary of parameters for the request

        Returns
        -------
        res : dict
        """
        response = requests.post(
            url=self.base_url + suffix,
            headers={
                "content_type": "application/json",
                "Authorization": f"Bearer {self.config.token.access_token}",
            },
            json=payload,
        )
        if 200 <= response.status_code < 300:
            print("Successfully uploaded!")
        else:
            return response.text

    def put(self):
        pass

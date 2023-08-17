from typing import Any, Optional

import requests
from requests import Response

from whitson.client.config import ClientConfig


class APIClient:
    def __init__(self, config: ClientConfig):
        self.base_url = f"http://{config.client_name}.whitson.com/api-external/v1"
        self.headers = {
            "content_type": "application/json",
            "Authorization": f"Bearer {config.token.access_token}",
        }

    def get(self, url: str, params: Optional[dict[str, Any]] = None) -> Response:
        response = requests.get(url=url, params=params, headers=self.headers)
        if not response:
            raise Exception("No information retrieved")
        return response

    def post(self, url: str, payload: Optional[dict[str, Any]]) -> str:
        """Perform a generic POST request to an arbitrary path in the API."""
        response = requests.post(
            url=url,
            headers=self.headers,
            json=payload,
        )
        if 200 <= response.status_code < 300:
            print("Successfully uploaded!")
        else:
            return response.text

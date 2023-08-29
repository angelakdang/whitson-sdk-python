import json
from typing import Any, Dict, Optional

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

    def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Response:
        response = requests.get(url=url, params=params, headers=self.headers)
        if not response:
            raise Exception("No information retrieved")
        return response

    def post(self, url: str, payload: Optional[Dict[str, Any]]) -> str:
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

    @staticmethod
    def get_total_pages(response: Response) -> int:
        pagination = json.loads(response.headers["X-Pagination"])
        return pagination["total_pages"]

    @staticmethod
    def filter_params(params: Dict[str, Any]):
        return {k: v for k, v in params.items() if v}

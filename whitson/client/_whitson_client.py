from typing import Any, Dict, Optional

from requests import Response

from whitson.client._api_client import APIClient
from whitson.client.api.fields import FieldsAPI
from whitson.client.api.production_data import ProductionDataAPI
from whitson.client.api.projects import ProjectsAPI
from whitson.client.api.wells import WellsAPI
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

        self.config = config
        self._api_client = APIClient(self.config)
        self.fields = FieldsAPI(self.config)
        self.wells = WellsAPI(self.config)
        self.projects = ProjectsAPI(self.config)
        self.production_data = ProductionDataAPI(self.config)

    def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Response:
        """Perform a generic GET request to an arbitrary path in the API."""
        return self._api_client.get(url=url, params=params)

    def post(self, url: str, payload: Optional[Dict[str, Any]] = None) -> str:
        """Perform a generic POST request to an arbitrary path in the API."""
        return self._api_client.post(url=url, payload=payload)

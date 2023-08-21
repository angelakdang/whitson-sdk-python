from dacite import from_dict

from whitson.client._api_client import APIClient
from whitson.client.dataclasses import Well


class WellsAPI(APIClient):
    def list(self, project_id):
        """Returns all the wells for a specified project."""
        response = self.get(
            url=f"{self.base_url}/wells", params={"project_id": project_id}
        )
        return [from_dict(data=r, data_class=Well) for r in response.json()]

    def retrieve(self, well_id: int = None, external_id: str = None):
        pass

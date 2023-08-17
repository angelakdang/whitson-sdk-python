from whitson.client._api_client import APIClient


class WellsAPI(APIClient):
    def list(self, project_id):
        response = self.get(
            url=f"{self.base_url}/wells", params={"project_id": project_id}
        )
        return response.json()

    def retrieve(self, well_id: int = None, external_id: str = None):
        pass

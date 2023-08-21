from whitson.client._api_client import APIClient
from whitson.client.config import ClientConfig


class ProductionDataAPI(APIClient):
    def __init__(self, config: ClientConfig):
        APIClient.__init__(self, config)
        self.p_wf_measured = None

    def retrieve(
        self,
        well_id: str = None,
    ):
        response = self.get(url=f"{self.base_url}/wells/{well_id}/production_data")
        self.p_wf_measured = [
            (data["date"], data["p_wf_measured"]) for data in response.json()
        ]
        return response.json()

    def insert(self):
        """Upload production data for a single well."""
        pass

    def insert_multiple(self):
        """Upload production data for multiple wells"""
        pass

    def delete(self, well_id: str, start_date: str = None, end_date: str = None):
        """Delete production data for a single well"""
        pass

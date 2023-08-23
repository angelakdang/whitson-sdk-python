from datetime import datetime

from dacite import from_dict

from whitson.client._api_client import APIClient
from whitson.client.dataclasses import ProductionData


class ProductionDataAPI(APIClient):
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

    def retrieve(self, well_id: str = None) -> ProductionData:
        data_formatted = {"well_id": str(well_id)}
        response = self.get(url=f"{self.base_url}/wells/{well_id}/production_data")
        data = response.json()
        for key in data[0].keys():
            if key != "well_id":
                data_formatted[key] = [
                    (
                        datetime.strptime(r["date"], ProductionDataAPI.DATE_FORMAT),
                        r[key],
                    )
                    for r in response.json()
                    if r[key]
                ]
        return from_dict(data=data_formatted, data_class=ProductionData)

    def insert(self):
        """Upload production data for a single well."""
        pass

    def insert_multiple(self):
        """Upload production data for multiple wells"""
        pass

    def delete(self, well_id: str, start_date: str = None, end_date: str = None):
        """Delete production data for a single well"""
        pass

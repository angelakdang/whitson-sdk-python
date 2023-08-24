from datetime import datetime

from dacite import from_dict

from whitson.client._api_client import APIClient
from whitson.client.dataclasses import Well


class WellsAPI(APIClient):
    DATE_FORMAT = "%Y-%m-%d"

    def list(self, project_id):
        """Returns all the wells for a specified project."""
        response = self.get(
            url=f"{self.base_url}/wells", params={"project_id": project_id}
        )
        return [from_dict(data=r, data_class=Well) for r in response.json()]

    def retrieve(self, well_id: int = None, external_id: str = None):
        pass

    def run_bhp_calc(self, well_id: int = None):
        response = self.get(url=f"{self.base_url}/wells/{well_id}/run_bhp_calculation")
        return response

    def retrieve_bhp_calcs(
        self,
        well_id: int = None,
        date: str = "",
        project_id: int = None,
        uwi_api: str = None,
        page: int = 1,
        page_size: int = 10,
    ):
        """Gets the BHP forecast calculation object attached to the well
        filtered by the provided arguments in the database.
        Returns a list of all BHP calculations from date and onwards if date is specified.
        Return all days if not specified.
        """
        # Should only input well_id OR uwi_api
        if well_id and uwi_api:
            raise ValueError("Specify well_id OR uwi_api; not both.")
        # Check for correct date format
        if date:
            try:
                datetime.strptime(date, WellsAPI.DATE_FORMAT)
            except ValueError:
                raise ValueError(
                    f"Incorrect date format. Should be: {WellsAPI.DATE_FORMAT}"
                )

        if well_id:
            params = {"date": date} if date else None
            response = self.get(
                url=f"{self.base_url}/wells/{well_id}/bhp_calculation", params=params
            )
            return response.json()
        else:
            # Filter out params; well_id not included
            # if it's specified, user is looking for return on single well
            all_params = {
                "date": date,
                "project_id": project_id,
                "uwi_api": uwi_api,
                "page": page,
                "page_size": page_size,
            }
            params = {k: v for k, v in all_params.items() if v}

            response = self.get(
                url=f"{self.base_url}/wells/bhp_calculation", params=params
            )
            return response.json()

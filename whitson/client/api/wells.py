import logging
from datetime import datetime
from typing import Dict, List, Union

from dacite import from_dict

from whitson.client._api_client import APIClient
from whitson.client.dataclasses import Well

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class WellsAPI(APIClient):
    DATE_FORMAT = "%Y-%m-%d"

    def list(self, project_id: int) -> List[Union[Well, None]]:
        """Returns all the wells for a specified project."""
        response = self.get(
            url=f"{self.base_url}/wells", params={"project_id": project_id}
        )
        return [from_dict(data=r, data_class=Well) for r in response.json()]

    def retrieve(self, well_id: int = None, external_id: str = None):
        pass

    def run_bhp_calc(self, well_id: int = None):
        """Run BHP calculations for a specified well."""
        response = self.get(url=f"{self.base_url}/wells/{well_id}/run_bhp_calculation")
        if response.status_code <= 202:
            logger.info(response.reason)
        else:
            raise RuntimeError(response.reason)

    def retrieve_bhp_calcs(
        self,
        well_id: int = None,
        date: str = "",
        project_id: int = None,
        uwi_api: str = None,
        page_size: int = 5000,  # max size
    ) -> Union[Dict, List[Dict]]:
        """Gets the BHP forecast calculation objects attached to the well

        Returns a list of all BHP calculations from date and onwards if date is specified.
        Return all days if not specified.

        Parameters
        ----------
        well_id: int
            Whitson well id
        date:
            Date in WellsAPI.DATE_FORMAT
        project_id: int
            Whitson project id
        uwi_api: str
            Unique well identifier as specified in the Whitson project.
            Can only specify well_id OR uwi_api, not both.
        page_size: int
            How large the results page will be. Max 5000.

        Returns
        -------
            Dictionary (for a well) or list of dictionaries (for multiple wells)
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
            # Return data for only one well
            params = {"date": date} if date else None
            response = self.get(
                url=f"{self.base_url}/wells/{well_id}/bhp_calculation", params=params
            )
            return response.json()
        else:
            # Return for all wells
            # Instantiate values
            page = 1
            result = []

            # Filter out params; well_id not included
            # if it's specified, user is looking for return on single well
            all_params = {
                "date": date,
                "project_id": project_id,
                "uwi_api": uwi_api,
                "page": page,
                "page_size": page_size,
            }
            params = APIClient.filter_params(all_params)
            logger.debug(f"Retrieving data for {params}")

            response = self.get(
                url=f"{self.base_url}/wells/bhp_calculation", params=params
            )
            result.extend(response.json())

            # If results are longer than one page
            if len(result) == page_size:
                logger.info("Results may be longer than one page. Retrieving...")
                while len(response.json()) > 0:
                    page += 1
                    params["page"] = page
                    response = self.get(
                        url=f"{self.base_url}/wells/bhp_calculation", params=params
                    )
                    logger.info(
                        f"Page: {page}, Result: {len(result)}, Params: {params}"
                    )
                    result.extend(response.json())
                    if page > 999:  # arbitrary stop point
                        break

            return result

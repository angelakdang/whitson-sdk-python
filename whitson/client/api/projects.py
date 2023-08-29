from typing import List, Union

from dacite import from_dict

from whitson.client._api_client import APIClient
from whitson.client.dataclasses import Project


class ProjectsAPI(APIClient):
    def list(self, field_id: int) -> List[Union[Project, None]]:
        """

        Parameters
        ----------
        field_id: int
            Whitson field id

        Returns
        -------
            List of Projects

        Examples
        -------
            List projects in field:

                >>> from whitson.client import WhitsonClient
                >>> client = WhitsonClient()
                >>> res = client.projects.list(field_id=1)
        """
        response = self.get(url=f"{self.base_url}/fields/{field_id}/projects")
        return [from_dict(data=f, data_class=Project) for f in response.json()]

    def retrieve(self, field_id: int, project_id: int) -> Union[Project, None]:
        """Retrieve a specified project from a specified field in Whitson.

        Parameters
        ----------
        field_id: int
            Whitson field id
        project_id: int
            Whitson project id

        Returns
        -------
            Project if it exists
        """
        # TODO: This function is exactly like fields.retrieve
        projects = self.list(field_id)
        project = [p for p in projects if p.id == project_id]
        if project:
            return project[0]
        else:
            return None

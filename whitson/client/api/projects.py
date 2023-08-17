from dacite import from_dict

from whitson.client._api_client import APIClient
from whitson.client.dataclasses import Project


class ProjectsAPI(APIClient):
    def list(self):
        response = self.get(url=f"{self.base_url}/projects")
        return [from_dict(data=f, data_class=Project) for f in response.json()]

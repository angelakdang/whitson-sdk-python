from dacite import from_dict

from whitson.client._api_client import APIClient
from whitson.client.dataclasses import Project


class ProjectsAPI(APIClient):
    def list(self, field_id):
        response = self.get(url=f"{self.base_url}/fields/{field_id}/projects")
        return [from_dict(data=f, data_class=Project) for f in response.json()]

    def retrieve(self, field_id, project_id):
        # TODO: This function is exactly like fields.retrieve
        projects = self.list(field_id)
        project = [p for p in projects if p.id == project_id]
        if project:
            return project[0]
        else:
            return None

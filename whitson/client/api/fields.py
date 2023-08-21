from dacite import from_dict

from whitson.client._api_client import APIClient
from whitson.client.dataclasses import Field


class FieldsAPI(APIClient):
    def list(self):
        response = self.get(url=f"{self.base_url}/fields")
        return [from_dict(data=f, data_class=Field) for f in response.json()]

    def retrieve(self, field_id: int):
        """Retrieve a single Field by id. </api-external/v1/fields>

        Parameters
        ----------
        field_id : int
            ID

        Returns
        -------
            Requested field or None if it doesn't exist

        Examples
        -------
            Get field by id:

                >>> from whitson.client import WhitsonClient
                >>> client = WhitsonClient()
                >>> res = client.fields.retrieve(field_id=1)
        """
        # TODO: This function is exactly like projects.retrieve
        fields = self.list()
        field = [f for f in fields if f.id == field_id]
        if field:
            return field[0]
        else:
            return None

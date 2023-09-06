# Whitson Python SDK

[![release](https://github.com/angelakdang/whitson-sdk-python/actions/workflows/release.yaml/badge.svg)](https://github.com/angelakdang/whitson-sdk-python/actions/actions?query=workflows:release)
[![GitHub](https://img.shields.io/github/license/angelakdang/whitson-sdk-python)](https://github.com/angelakdang/whitson-sdk-python/blob/master/LICENSE.txt)
[![PyPI version](https://badge.fury.io/py/whitson-sdk-python.svg)](https://pypi.org/project/whitson-sdk-python)

This is the Whitson Python SDK for developers, data scientists, and engineers working with
[Whitson+](https://whitson.com/software/).

The API documentation is accessible with the client name:
[https://<CLIENT_NAME>.whitson.com/api-external/swagger/]()

The source code is located in the `whitson/client` directory.

## Example usage

Store your secrets in a `.env` file:
```bash
WHITSON_CLIENT_NAME=<client-name>
WHITSON_CLIENT_ID=<client-id>
WHITSON_CLIENT_SECRET=<client-secret>
PATH_TO_TOKEN=token.json
```

If you have it, store your token in a JSON file (only the `access_token` key is required):
```json
 {
   'access_token': '<access-token-value>',
   'scope': 'get:api post:api delete:api',
   'expires_in': 86400,
   'token_type': 'Bearer',
   'issued_at': 1692136969.7024412
 }
```

In a Python file:
```python
import json
from dacite import from_dict
from decouple import config
from whitson.client import WhitsonClient
from whitson.client.config import Token, ClientConfig

# Get environment variables
client_name = config("WHITSON_CLIENT_NAME")
client_id = config("WHITSON_CLIENT_ID")
client_secret = config("WHITSON_CLIENT_SECRET")
path_to_token = config("PATH_TO_TOKEN")

# CONNECT TO WHITSON
# Check for access token
with open(path_to_token) as f:
    token = from_dict(data=json.load(f), data_class=Token)

# Define configuration parameters to retrieve access token
# If no token is specified, a new one will be requested and the output printed.
# If certain certificates are required for data to be requested, this can be specified in a PEM file
config = ClientConfig(
    token=token,
    client_name=client_name,
    client_id=client_id,
    client_secret=client_secret,
    pem_path="src/custom_cacerts.pem",  # optional, may be required to traverse firewall
)

# Instantiate client and retrieve data
client = WhitsonClient(config)

# Constants
FIELD_ID = 1
PROJECT_ID = 159

# Get field
field = client.fields.retrieve(field_id=FIELD_ID)
print(f"{field.name} field retrieved.")

# Get project associated with field
project = client.projects.retrieve(field_id=field.id, project_id=PROJECT_ID)
print(f"{project.name} project retrieved.")

# Get wells associated to the project
wells = client.wells.list(project_id=project.id)
well = wells[0]
print(f"{well.name} retrieved.")

# Run BHP calculations for a well
client.wells.run_bhp_calc(well_id=well.id)
print("BHP calculations complete.")

# Retrieve BHP calculations for a well
bhp_corr_well = client.wells.retrieve_bhp_calcs(well_id=well.id)
print(f"BHP calculations retrieved for {well.name} ({well.id}).")

# Retrieve all BHP calculations in a project
bhp_corr = client.wells.retrieve_bhp_calcs(project_id=project.id)
print("BHP calculations retrieved for all wells.")
```
## Improvements

- [ ] The `list()` and `retrieve()` functions in the `api/` classes are very similiar. Need to find a way to
  simplify this.
- [ ] Tests need to be written to show expected result when retrieving data

## Acknowledgements

I learned a great deal from the amazing and talented people at [Cognite](https://www.cognite.com/en/) and this
repository is _heavily_ based off of the structure of the publicly available
[Cognite Python SDK](https://github.com/cognitedata/cognite-sdk-python).
Thank you for the incredible experience and the continued learning your resources have provided me.

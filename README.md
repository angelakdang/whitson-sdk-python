# Whitson Python SDK
This is the Whitson Python SDK for developers, data scientists, and engineers working with
[Whitson+](https://whitson.com/software/).

The source code is located in the `whitson/client` directory.

Example usage:

```python
import json
from decouple import config
from dacite import from_dict
from whitson.client import Token, ClientConfig, WhitsonClient


# Define connection details as environment variables
CLIENT_NAME = config("WHITSON_CLIENT_NAME")
CLIENT_ID = config("WHITSON_CLIENT_ID")
CLIENT_SECRET = config("WHITSON_CLIENT_SECRET")

# Check for access token
with open("token.json") as f:
    token = from_dict(data=json.load(f), data_class=Token)

# Define configuration parameters to retrieve access token
# If no token is specified, a new one will be requested and the output printed.
# If certain certificates are required for data to be requested, this can be specified in a PEM file
config = ClientConfig(
    token=token,
    client_name=CLIENT_NAME,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    pem_path="custom_cacerts.pem"
)

# Instantiate client and retrieve data
client = WhitsonClient(config)

# Example
project_id = 161
well_id = 228368
result = client.get(suffix=f"wells/{well_id}/bhp_calculation", params={"project_id": project_id})
```

The access token can be stored in a `JSON` file as shown below:

```json
 {
   'access_token': '<access-token-value>',
   'scope': 'get:api post:api delete:api',
   'expires_in': 86400,
   'token_type': 'Bearer',
   'issued_at': 1692136969.7024412
 }
```

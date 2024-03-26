# Fleet Protocol HTTP API Client

This is a Client for the Fleet Protocol HTTP API. You can find the Fleet Protocol HTTP API repository [here](https://github.com/bringauto/fleet-protocol-http-api).
The HTTP API is described by the `openapi/openapi.yaml` according to [OpenAPI Specification](https://openapis.org).
A full specification can be found in the `openapi` folder in the root folder.

## Auto-generated code
The auto-generated code can be found in the `fleet_http_client_python` folder.
The code is generated using the `openapi-generator-cli` tool. The code is generated using the `openapi.yaml` file.
DO NOT edit the auto-generated code manually.

## Documentation
The auto-generated documentation for the client models and API is in the `fleet_http_client_python/docs` folder.

# Installation
To install the client, run
```bash
pip install git+https://github.com/bringauto/fleet-http-api-client.git
```

## Client re-generation
If you want to re-generate the client code with the new specification, you first have to replace the specification in the root folder.
Then you can run the `regen.sh` script (from the root folder).

# Requirements
Python 3.10.12+


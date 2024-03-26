# PayloadData

Payload data in \"JSON\" or \"BASE64\" format, depending on the encoding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fleet_http_client_python.models.payload_data import PayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadData from a JSON string
payload_data_instance = PayloadData.from_json(json)
# print the JSON string representation of the object
print(PayloadData.to_json())

# convert the object into a dict
payload_data_dict = payload_data_instance.to_dict()
# create an instance of PayloadData from a dict
payload_data_form_dict = payload_data.from_dict(payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



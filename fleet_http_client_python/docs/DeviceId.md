# DeviceId

Id of the device described with an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **int** | Id (unsigned integer) of the module containing the device. | 
**type** | **int** | Unsigned integer. | 
**role** | **str** | String description of the device role. It follows pattern ^[a-z0-9_]+$. | 
**name** | **str** | UTF-8 encoded string. | 

## Example

```python
from fleet_http_client_python.models.device_id import DeviceId

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceId from a JSON string
device_id_instance = DeviceId.from_json(json)
# print the JSON string representation of the object
print(DeviceId.to_json())

# convert the object into a dict
device_id_dict = device_id_instance.to_dict()
# create an instance of DeviceId from a dict
device_id_form_dict = device_id.from_dict(device_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



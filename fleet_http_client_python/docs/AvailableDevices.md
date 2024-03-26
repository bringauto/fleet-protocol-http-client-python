# AvailableDevices

List of Modules containint at least one device (specified by device Id) OR Module containing at least one device (specified by device Id).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **int** | Id (unsigned integer) of the module. | 
**device_list** | [**List[DeviceId]**](DeviceId.md) | List of Ids of devices contained in the module. | 

## Example

```python
from fleet_http_client_python.models.available_devices import AvailableDevices

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableDevices from a JSON string
available_devices_instance = AvailableDevices.from_json(json)
# print the JSON string representation of the object
print(AvailableDevices.to_json())

# convert the object into a dict
available_devices_dict = available_devices_instance.to_dict()
# create an instance of AvailableDevices from a dict
available_devices_form_dict = available_devices.from_dict(available_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



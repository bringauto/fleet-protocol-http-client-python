# Car

A car assigned to a particular company.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Name of the company, following a pattern ^[0-9a-z_]+$ | 
**car_name** | **str** | Name of the Car, following a pattern ^[0-9a-z_]+$ | 

## Example

```python
from fleet_http_client_python.models.car import Car

# TODO update the JSON string below
json = "{}"
# create an instance of Car from a JSON string
car_instance = Car.from_json(json)
# print the JSON string representation of the object
print(Car.to_json())

# convert the object into a dict
car_dict = car_instance.to_dict()
# create an instance of Car from a dict
car_form_dict = car.from_dict(car_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



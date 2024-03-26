# fleet_http_client_python.ModuleApi

All URIs are relative to */v2/protocol*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_devices**](ModuleApi.md#available_devices) | **GET** /available-devices/{company_name}/{car_name} | 


# **available_devices**
> AvailableDevices available_devices(company_name, car_name, module_id=module_id)



Return device Ids for all devices available for contained in the specified car.<br> For a single car module, the device Ids are returned as an object containing module Id and the list of device Ids. <br> If a module Id is specified, only a single such object is returned. <br> Otherwise, a list of such objects is returned, one for each module contained in the car. <br>

### Example

* Api Key Authentication (AdminAuth):
* OAuth Authentication (oAuth2AuthCode):

```python
import fleet_http_client_python
from fleet_http_client_python.models.available_devices import AvailableDevices
from fleet_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/protocol
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_http_client_python.Configuration(
    host = "/v2/protocol"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AdminAuth
configuration.api_key['AdminAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AdminAuth'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fleet_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_http_client_python.ModuleApi(api_client)
    company_name = 'test_company' # str | Name of the company, following a pattern ^[0-9a-z_]+$.
    car_name = 'test_car' # str | Name of the Car, following a pattern ^[0-9a-z_]+$.
    module_id = 47 # int | An Id of module, an unsigned integer. (optional)

    try:
        api_response = api_instance.available_devices(company_name, car_name, module_id=module_id)
        print("The response of ModuleApi->available_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->available_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_name** | **str**| Name of the company, following a pattern ^[0-9a-z_]+$. | 
 **car_name** | **str**| Name of the Car, following a pattern ^[0-9a-z_]+$. | 
 **module_id** | **int**| An Id of module, an unsigned integer. | [optional] 

### Return type

[**AvailableDevices**](AvailableDevices.md)

### Authorization

[AdminAuth](../README.md#AdminAuth), [oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available devices. |  -  |
**404** | Cannot display available devices. Either company, car or module specified in the request does not exist. |  -  |
**500** | Cannot display available devices due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


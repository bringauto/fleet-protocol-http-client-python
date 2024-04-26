# fleet_http_client_python.CarApi

All URIs are relative to */v2/protocol*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_cars**](CarApi.md#available_cars) | **GET** /cars | 


# **available_cars**
> List[Car] available_cars(wait=wait, since=since)



Return list of available cars for all companies registered in the database.

### Example

* Api Key Authentication (AdminAuth):
* OAuth Authentication (oAuth2AuthCode):

```python
import fleet_http_client_python
from fleet_http_client_python.models.car import Car
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
    api_instance = fleet_http_client_python.CarApi(api_client)
    wait = False # bool | An empty parameter. If specified, the method waits for predefined period of time, until some data to be sent in response are available. (optional) (default to False)
    since = 0 # int | A Unix timestamp; if specified, the method returns all messages inclusivelly newer than the specified timestamp \\ (i.e., messages with timestamp greater than or equal to the 'since' timestamp) (optional) (default to 0)

    try:
        api_response = api_instance.available_cars(wait=wait, since=since)
        print("The response of CarApi->available_cars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarApi->available_cars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wait** | **bool**| An empty parameter. If specified, the method waits for predefined period of time, until some data to be sent in response are available. | [optional] [default to False]
 **since** | **int**| A Unix timestamp; if specified, the method returns all messages inclusivelly newer than the specified timestamp \\ (i.e., messages with timestamp greater than or equal to the &#39;since&#39; timestamp) | [optional] [default to 0]

### Return type

[**List[Car]**](Car.md)

### Authorization

[AdminAuth](../README.md#AdminAuth), [oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available cars. |  -  |
**500** | Cannot display available cars due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


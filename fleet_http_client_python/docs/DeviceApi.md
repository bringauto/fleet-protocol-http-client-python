# fleet_http_client_python.DeviceApi

All URIs are relative to */v2/protocol*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_commands**](DeviceApi.md#list_commands) | **GET** /command/{company_name}/{car_name} | 
[**list_statuses**](DeviceApi.md#list_statuses) | **GET** /status/{company_name}/{car_name} | 
[**send_commands**](DeviceApi.md#send_commands) | **POST** /command/{company_name}/{car_name} | 
[**send_statuses**](DeviceApi.md#send_statuses) | **POST** /status/{company_name}/{car_name} | 


# **list_commands**
> List[Message] list_commands(company_name, car_name, since=since, wait=wait)



Returns list of the Device Commands.

### Example

* Api Key Authentication (AdminAuth):
* OAuth Authentication (oAuth2AuthCode):

```python
import fleet_http_client_python
from fleet_http_client_python.models.message import Message
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
    api_instance = fleet_http_client_python.DeviceApi(api_client)
    company_name = 'test_company' # str | Name of the company, following a pattern ^[0-9a-z_]+$.
    car_name = 'test_car' # str | Name of the Car, following a pattern ^[0-9a-z_]+$.
    since = 0 # int | A Unix timestamp; if specified, the method returns all messages inclusivelly newer than the specified timestamp \\ (i.e., messages with timestamp greater than or equal to the 'since' timestamp) (optional) (default to 0)
    wait = False # bool | An empty parameter. If specified, the method waits for predefined period of time, until some data to be sent in response are available. (optional) (default to False)

    try:
        api_response = api_instance.list_commands(company_name, car_name, since=since, wait=wait)
        print("The response of DeviceApi->list_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->list_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_name** | **str**| Name of the company, following a pattern ^[0-9a-z_]+$. | 
 **car_name** | **str**| Name of the Car, following a pattern ^[0-9a-z_]+$. | 
 **since** | **int**| A Unix timestamp; if specified, the method returns all messages inclusivelly newer than the specified timestamp \\ (i.e., messages with timestamp greater than or equal to the &#39;since&#39; timestamp) | [optional] [default to 0]
 **wait** | **bool**| An empty parameter. If specified, the method waits for predefined period of time, until some data to be sent in response are available. | [optional] [default to False]

### Return type

[**List[Message]**](Message.md)

### Authorization

[AdminAuth](../README.md#AdminAuth), [oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of commands. |  -  |
**404** | The commands cannot be displayed. Either company, car or device specified in the request does not exist. |  -  |
**500** | The commands cannot be displayed due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_statuses**
> List[Message] list_statuses(company_name, car_name, since=since, wait=wait)



It returns list of the Device Statuses.

### Example

* Api Key Authentication (AdminAuth):
* OAuth Authentication (oAuth2AuthCode):

```python
import fleet_http_client_python
from fleet_http_client_python.models.message import Message
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
    api_instance = fleet_http_client_python.DeviceApi(api_client)
    company_name = 'test_company' # str | Name of the company, following a pattern ^[0-9a-z_]+$.
    car_name = 'test_car' # str | Name of the Car, following a pattern ^[0-9a-z_]+$.
    since = 0 # int | A Unix timestamp; if specified, the method returns all messages inclusivelly newer than the specified timestamp \\ (i.e., messages with timestamp greater than or equal to the 'since' timestamp) (optional) (default to 0)
    wait = False # bool | An empty parameter. If specified, the method waits for predefined period of time, until some data to be sent in response are available. (optional) (default to False)

    try:
        api_response = api_instance.list_statuses(company_name, car_name, since=since, wait=wait)
        print("The response of DeviceApi->list_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->list_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_name** | **str**| Name of the company, following a pattern ^[0-9a-z_]+$. | 
 **car_name** | **str**| Name of the Car, following a pattern ^[0-9a-z_]+$. | 
 **since** | **int**| A Unix timestamp; if specified, the method returns all messages inclusivelly newer than the specified timestamp \\ (i.e., messages with timestamp greater than or equal to the &#39;since&#39; timestamp) | [optional] [default to 0]
 **wait** | **bool**| An empty parameter. If specified, the method waits for predefined period of time, until some data to be sent in response are available. | [optional] [default to False]

### Return type

[**List[Message]**](Message.md)

### Authorization

[AdminAuth](../README.md#AdminAuth), [oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of device statuses. |  -  |
**404** | The statuses cannot be displayed. Either company, car or device specified in the request does not exist. |  -  |
**500** | The statuses cannot be displayed due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_commands**
> send_commands(company_name, car_name, message=message)



It adds new device Commands.

### Example

* Api Key Authentication (AdminAuth):
* OAuth Authentication (oAuth2AuthCode):

```python
import fleet_http_client_python
from fleet_http_client_python.models.message import Message
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
    api_instance = fleet_http_client_python.DeviceApi(api_client)
    company_name = 'test_company' # str | Name of the company, following a pattern ^[0-9a-z_]+$.
    car_name = 'test_car' # str | Name of the Car, following a pattern ^[0-9a-z_]+$.
    message = [{"device_id":{"module_id":47,"type":2,"role":"test_device","name":"Test Device"},"payload":{"message_type":"COMMAND","encoding":"BASE64","data":"U2F5IGhlbGxv"}}] # List[Message] | Commands to be executed by the device. (optional)

    try:
        api_instance.send_commands(company_name, car_name, message=message)
    except Exception as e:
        print("Exception when calling DeviceApi->send_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_name** | **str**| Name of the company, following a pattern ^[0-9a-z_]+$. | 
 **car_name** | **str**| Name of the Car, following a pattern ^[0-9a-z_]+$. | 
 **message** | [**List[Message]**](Message.md)| Commands to be executed by the device. | [optional] 

### Return type

void (empty response body)

### Authorization

[AdminAuth](../README.md#AdminAuth), [oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The commands have been sent. |  -  |
**404** | The commands have not been sent. Either company, car or device specified in the request does not exist.&#39; |  -  |
**500** | The commands have not been sent due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_statuses**
> send_statuses(company_name, car_name, message=message)



Add statuses received from the Device.

### Example

* Api Key Authentication (AdminAuth):
* OAuth Authentication (oAuth2AuthCode):

```python
import fleet_http_client_python
from fleet_http_client_python.models.message import Message
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
    api_instance = fleet_http_client_python.DeviceApi(api_client)
    company_name = 'test_company' # str | Name of the company, following a pattern ^[0-9a-z_]+$.
    car_name = 'test_car' # str | Name of the Car, following a pattern ^[0-9a-z_]+$.
    message = [{"device_id":{"module_id":47,"type":2,"role":"test_device","name":"Test Device"},"payload":{"message_type":"STATUS","encoding":"BASE64","data":"QnJpbmdBdXRv"}}] # List[Message] | Statuses to be send by the device. (optional)

    try:
        api_instance.send_statuses(company_name, car_name, message=message)
    except Exception as e:
        print("Exception when calling DeviceApi->send_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_name** | **str**| Name of the company, following a pattern ^[0-9a-z_]+$. | 
 **car_name** | **str**| Name of the Car, following a pattern ^[0-9a-z_]+$. | 
 **message** | [**List[Message]**](Message.md)| Statuses to be send by the device. | [optional] 

### Return type

void (empty response body)

### Authorization

[AdminAuth](../README.md#AdminAuth), [oAuth2AuthCode](../README.md#oAuth2AuthCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The statuses have been sent. |  -  |
**404** | The statuses could not been sent. Either company, car or device specified in the request does not exist. |  -  |
**500** | The statuses could not been sent due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


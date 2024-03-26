# fleet_http_client_python.LoginApi

All URIs are relative to */v2/protocol*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginApi.md#login) | **GET** /login | 
[**token_get**](LoginApi.md#token_get) | **GET** /token_get | 
[**token_refresh**](LoginApi.md#token_refresh) | **GET** /token_refresh | 


# **login**
> login(device=device)



Login using keycloak. If empty device is specified, will generate a url and device code used to authenticate a device. Tries to get token if device code is specified.

### Example


```python
import fleet_http_client_python
from fleet_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/protocol
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_http_client_python.Configuration(
    host = "/v2/protocol"
)


# Enter a context with an instance of the API client
with fleet_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_http_client_python.LoginApi(api_client)
    device = 'e-VZfSM_-_TyPElL3i94...' # str | Device code used for assisted authentication. (optional)

    try:
        api_instance.login(device=device)
    except Exception as e:
        print("Exception when calling LoginApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device code used for assisted authentication. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns either a standard keycloak token or a json used to authenticate a device. |  -  |
**302** | Redirect to keycloak authentication. |  -  |
**500** | Login failed due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_get**
> token_get(state=state, session_state=session_state, iss=iss, code=code)



Callback endpoint for keycloak to receive jwt token.

### Example


```python
import fleet_http_client_python
from fleet_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/protocol
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_http_client_python.Configuration(
    host = "/v2/protocol"
)


# Enter a context with an instance of the API client
with fleet_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_http_client_python.LoginApi(api_client)
    state = 'your_state_info' # str | State returned by keycloak authentication. (optional)
    session_state = '167e141d-2f55-4d...' # str | Session state returned by keycloak authentication. (optional)
    iss = 'http%3A%2F%2Flocalhost%3A8081%2Frealms%2Fmaster' # str | Code issuer returned by keycloak authentication. (optional)
    code = '5dea27d2-4b2d-48...' # str | Code used for jwt token generation returned by keycloak authentication. (optional)

    try:
        api_instance.token_get(state=state, session_state=session_state, iss=iss, code=code)
    except Exception as e:
        print("Exception when calling LoginApi->token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| State returned by keycloak authentication. | [optional] 
 **session_state** | **str**| Session state returned by keycloak authentication. | [optional] 
 **iss** | **str**| Code issuer returned by keycloak authentication. | [optional] 
 **code** | **str**| Code used for jwt token generation returned by keycloak authentication. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a standard keycloak token. |  -  |
**500** | Login failed due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_refresh**
> token_refresh(refresh_token)



Endpoint to receive jwt token from refresh token.

### Example


```python
import fleet_http_client_python
from fleet_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/protocol
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_http_client_python.Configuration(
    host = "/v2/protocol"
)


# Enter a context with an instance of the API client
with fleet_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_http_client_python.LoginApi(api_client)
    refresh_token = 'eyJhbGciOiJIUzI1NiIsI...' # str | Refresh token used for jwt token generation.

    try:
        api_instance.token_refresh(refresh_token)
    except Exception as e:
        print("Exception when calling LoginApi->token_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**| Refresh token used for jwt token generation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a new standard keycloak token. |  -  |
**500** | Token refresh failed due to internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# eliona.api_client.VersionApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api**](VersionApi.md#get_open_api) | **GET** /version/openapi.json | OpenAPI specification for this API version
[**get_version**](VersionApi.md#get_version) | **GET** /version | Version of the API


# **get_open_api**
> get_open_api()

OpenAPI specification for this API version

Gets specification for this API version as an openapi.json file.

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import version_api
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = version_api.VersionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # OpenAPI specification for this API version
        api_instance.get_open_api()
    except eliona.api_client.ApiException as e:
        print("Exception when calling VersionApi->get_open_api: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the openapi.json file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_version()

Version of the API

Gets information about the APIs version.

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import version_api
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = version_api.VersionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Version of the API
        api_response = api_instance.get_version()
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling VersionApi->get_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the APIs version. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


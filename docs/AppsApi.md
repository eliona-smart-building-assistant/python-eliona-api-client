# eliona.api_client.AppsApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_by_name**](AppsApi.md#get_app_by_name) | **GET** /apps/{app-name} | Information about an app
[**get_patch_by_name**](AppsApi.md#get_patch_by_name) | **GET** /apps/{app-name}/patches/{patch-name} | Information about a patch for an app
[**patch_app_by_name**](AppsApi.md#patch_app_by_name) | **PATCH** /apps/{app-name} | Update an app
[**patch_patch_by_name**](AppsApi.md#patch_patch_by_name) | **PATCH** /apps/{app-name}/patches/{patch-name} | Updates a patch


# **get_app_by_name**
> App get_app_by_name(app_name)

Information about an app

Gets information about an app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import apps_api
from eliona.api_client.model.app import App
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apps_api.AppsApi(api_client)
    app_name = "weather" # str | The name of the app

    # example passing only required values which don't have defaults set
    try:
        # Information about an app
        api_response = api_instance.get_app_by_name(app_name)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppsApi->get_app_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The name of the app |

### Return type

[**App**](App.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned information about an app. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_patch_by_name**
> Patch get_patch_by_name(app_name, patch_name)

Information about a patch for an app

Gets information about a patch for an app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import apps_api
from eliona.api_client.model.patch import Patch
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apps_api.AppsApi(api_client)
    app_name = "weather" # str | The name of the app
    patch_name = "2.0.0" # str | The name of the patch

    # example passing only required values which don't have defaults set
    try:
        # Information about a patch for an app
        api_response = api_instance.get_patch_by_name(app_name, patch_name)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppsApi->get_patch_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The name of the app |
 **patch_name** | **str**| The name of the patch |

### Return type

[**Patch**](Patch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned information about a patch for an app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_app_by_name**
> patch_app_by_name(app_name)

Update an app

Update properties of an app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import apps_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apps_api.AppsApi(api_client)
    app_name = "weather" # str | The name of the app
    registered = True # bool | Marks that the app is now initialized and installed. Further request to get app information returns { \"registered\": true } (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an app
        api_instance.patch_app_by_name(app_name)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppsApi->patch_app_by_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an app
        api_instance.patch_app_by_name(app_name, registered=registered)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppsApi->patch_app_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The name of the app |
 **registered** | **bool**| Marks that the app is now initialized and installed. Further request to get app information returns { \&quot;registered\&quot;: true } | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_patch_by_name**
> patch_patch_by_name(app_name, patch_name)

Updates a patch

Updates properties of a patch for an app.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import apps_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = apps_api.AppsApi(api_client)
    app_name = "weather" # str | The name of the app
    patch_name = "2.0.0" # str | The name of the patch
    apply = True # bool | Marks that the patch is now applied. Further request to get patch information returns { \"applied\": true } (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a patch
        api_instance.patch_patch_by_name(app_name, patch_name)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppsApi->patch_patch_by_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a patch
        api_instance.patch_patch_by_name(app_name, patch_name, apply=apply)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppsApi->patch_patch_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The name of the app |
 **patch_name** | **str**| The name of the patch |
 **apply** | **bool**| Marks that the patch is now applied. Further request to get patch information returns { \&quot;applied\&quot;: true } | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the patch for the app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


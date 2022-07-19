# eliona.api_client.AppApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_patch_by_name**](AppApi.md#apply_patch_by_name) | **PUT** /patch/{app-name}/{patch-name}/apply | Marks a patch in eliona as applied
[**get_app_by_name**](AppApi.md#get_app_by_name) | **GET** /app/{app-name} | Information about an app
[**get_patch_by_name**](AppApi.md#get_patch_by_name) | **GET** /patch/{app-name}/{patch-name} | Information about a patch for an app
[**register_app_by_name**](AppApi.md#register_app_by_name) | **PUT** /app/{app-name}/register | Marks an app in eliona as registered


# **apply_patch_by_name**
> apply_patch_by_name(app_name, patch_name)

Marks a patch in eliona as applied

Marks that the patch is now applied. Further request to get patch information returns { \"applied\": true }

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import app_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = app_api.AppApi(api_client)
    app_name = "weather" # str | The name of the app
    patch_name = "2.0.0" # str | The name of the patch

    # example passing only required values which don't have defaults set
    try:
        # Marks a patch in eliona as applied
        api_instance.apply_patch_by_name(app_name, patch_name)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppApi->apply_patch_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The name of the app |
 **patch_name** | **str**| The name of the patch |

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
**200** | Successfully applied the patch for the app in eliona |  -  |
**400** | Unable to apply patch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_by_name**
> App get_app_by_name(app_name)

Information about an app

Gets information about an app. Can used to determine if an app is already registered or not.

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import app_api
from eliona.api_client.model.app import App
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = app_api.AppApi(api_client)
    app_name = "weather" # str | The name of the app

    # example passing only required values which don't have defaults set
    try:
        # Information about an app
        api_response = api_instance.get_app_by_name(app_name)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppApi->get_app_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The name of the app |

### Return type

[**App**](App.md)

### Authorization

No authorization required

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

Gets information about a patch for an app. Can used to determine if the patch is already applied or not.

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import app_api
from eliona.api_client.model.patch import Patch
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = app_api.AppApi(api_client)
    app_name = "weather" # str | The name of the app
    patch_name = "2.0.0" # str | The name of the patch

    # example passing only required values which don't have defaults set
    try:
        # Information about a patch for an app
        api_response = api_instance.get_patch_by_name(app_name, patch_name)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppApi->get_patch_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The name of the app |
 **patch_name** | **str**| The name of the patch |

### Return type

[**Patch**](Patch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned information about a patch for an app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_app_by_name**
> register_app_by_name(app_name)

Marks an app in eliona as registered

Marks that the app is now initialized and installed. Further request to get app information returns { \"registered\": true }

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import app_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = app_api.AppApi(api_client)
    app_name = "weather" # str | The name of the app

    # example passing only required values which don't have defaults set
    try:
        # Marks an app in eliona as registered
        api_instance.register_app_by_name(app_name)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AppApi->register_app_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The name of the app |

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
**200** | Successfully registered the app in eliona |  -  |
**400** | Unable to register app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


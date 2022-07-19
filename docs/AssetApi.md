# io.eliona.api-client.AssetApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_by_id**](AssetApi.md#get_asset_by_id) | **GET** /asset/{asset-id} | Information about an Asset
[**get_asset_children**](AssetApi.md#get_asset_children) | **GET** /asset/{asset-id}/children | Get children for an asset
[**get_asset_parents**](AssetApi.md#get_asset_parents) | **GET** /asset/{asset-id}/parents | Get the parents for an asset
[**post_asset**](AssetApi.md#post_asset) | **POST** /asset | Create or update an asset
[**set_asset_parents**](AssetApi.md#set_asset_parents) | **PUT** /asset/{asset-id}/parents | Set or replace parents for an asset


# **get_asset_by_id**
> Asset get_asset_by_id(asset_id)

Information about an Asset

Gets information about an asset.

### Example


```python
import time
import io.eliona.api-client
from io.eliona.api-client.api import asset_api
from io.eliona.api-client.model.asset import Asset
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api-client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with io.eliona.api-client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = asset_api.AssetApi(api_client)
    asset_id = 4711 # int | The id of the asset

    # example passing only required values which don't have defaults set
    try:
        # Information about an Asset
        api_response = api_instance.get_asset_by_id(asset_id)
        pprint(api_response)
    except io.eliona.api-client.ApiException as e:
        print("Exception when calling AssetApi->get_asset_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset |

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the asset by id. |  -  |
**404** | Asset with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_children**
> [AssetRelation] get_asset_children(asset_id)

Get children for an asset

Returns a list of asset ids which are children for an asset

### Example


```python
import time
import io.eliona.api-client
from io.eliona.api-client.api import asset_api
from io.eliona.api-client.model.asset_relation import AssetRelation
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api-client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with io.eliona.api-client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = asset_api.AssetApi(api_client)
    asset_id = 4711 # int | The id of the asset

    # example passing only required values which don't have defaults set
    try:
        # Get children for an asset
        api_response = api_instance.get_asset_children(asset_id)
        pprint(api_response)
    except io.eliona.api-client.ApiException as e:
        print("Exception when calling AssetApi->get_asset_children: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset |

### Return type

[**[AssetRelation]**](AssetRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned children |  -  |
**404** | Asset with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_parents**
> [AssetRelation] get_asset_parents(asset_id)

Get the parents for an asset

Returns the asset ids which are the parents for an asset

### Example


```python
import time
import io.eliona.api-client
from io.eliona.api-client.api import asset_api
from io.eliona.api-client.model.asset_relation import AssetRelation
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api-client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with io.eliona.api-client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = asset_api.AssetApi(api_client)
    asset_id = 4711 # int | The id of the asset

    # example passing only required values which don't have defaults set
    try:
        # Get the parents for an asset
        api_response = api_instance.get_asset_parents(asset_id)
        pprint(api_response)
    except io.eliona.api-client.ApiException as e:
        print("Exception when calling AssetApi->get_asset_parents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset |

### Return type

[**[AssetRelation]**](AssetRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned parent |  -  |
**404** | Asset with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset**
> Asset post_asset(asset)

Create or update an asset

Creates an asset if no asset with the same projectId and globalAssetIdentifier already exists. If there is such an asset, the asset is updated.

### Example


```python
import time
import io.eliona.api-client
from io.eliona.api-client.api import asset_api
from io.eliona.api-client.model.asset import Asset
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api-client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with io.eliona.api-client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = asset_api.AssetApi(api_client)
    asset = Asset(
        id=4711,
        project_id="99",
        global_asset_identifier="zurich_swiss",
        name="Station Zurich",
        asset_type="asset_type_example",
        latitude=47.3667,
        longitude=8.55,
        description="Weather station Zurich, Swiss",
        tags=["weather","location"],
    ) # Asset | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an asset
        api_response = api_instance.post_asset(asset)
        pprint(api_response)
    except io.eliona.api-client.ApiException as e:
        print("Exception when calling AssetApi->post_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**Asset**](Asset.md)|  |

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing asset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_parents**
> set_asset_parents(asset_id, asset_relation)

Set or replace parents for an asset

Sets or replaces the parent asset ids for an asset

### Example


```python
import time
import io.eliona.api-client
from io.eliona.api-client.api import asset_api
from io.eliona.api-client.model.asset_relation import AssetRelation
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api-client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with io.eliona.api-client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = asset_api.AssetApi(api_client)
    asset_id = 4711 # int | The id of the asset
    asset_relation = [
        AssetRelation(
            related_asset_id=4712,
            type="location",
        ),
    ] # [AssetRelation] | 

    # example passing only required values which don't have defaults set
    try:
        # Set or replace parents for an asset
        api_instance.set_asset_parents(asset_id, asset_relation)
    except io.eliona.api-client.ApiException as e:
        print("Exception when calling AssetApi->set_asset_parents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset |
 **asset_relation** | [**[AssetRelation]**](AssetRelation.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully set asset parent |  -  |
**404** | Asset with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


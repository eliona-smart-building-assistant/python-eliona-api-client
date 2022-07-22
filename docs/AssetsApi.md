# eliona.api_client.AssetsApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_by_id**](AssetsApi.md#get_asset_by_id) | **GET** /assets/{asset-id} | Information about an asset
[**get_assets**](AssetsApi.md#get_assets) | **GET** /assets | Information about assets
[**put_asset**](AssetsApi.md#put_asset) | **PUT** /assets | Create or update an asset


# **get_asset_by_id**
> Asset get_asset_by_id(asset_id)

Information about an asset

Gets information about an asset.

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = 4711 # int | The id of the asset
    with_children = False # bool | Gets also the the children hierarchy (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Information about an asset
        api_response = api_instance.get_asset_by_id(asset_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about an asset
        api_response = api_instance.get_asset_by_id(asset_id, with_children=with_children)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset |
 **with_children** | **bool**| Gets also the the children hierarchy | [optional] if omitted the server will use the default value of False

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

# **get_assets**
> [Asset] get_assets()

Information about assets

Gets a list of assets

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Information about assets
        api_response = api_instance.get_assets()
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->get_assets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Asset]**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset**
> Asset put_asset(asset)

Create or update an asset

Creates an asset if no asset with the same projectId and globalAssetIdentifier already exists. If there is such an asset, the asset is updated.

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset = Asset(
        project_id="99",
        global_asset_identifier="zurich_swiss",
        name="Station Zurich",
        asset_type="asset_type_example",
        latitude=47.3667,
        longitude=8.55,
        description="Weather station Zurich, Swiss",
        parent_functional_asset_id=4712,
        parent_locational_asset_id=4712,
        tags=["weather","location"],
    ) # Asset | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an asset
        api_response = api_instance.put_asset(asset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->put_asset: %s\n" % e)
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


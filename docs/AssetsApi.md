# eliona.api_client.AssetsApi

All URIs are relative to *https://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset_by_id**](AssetsApi.md#delete_asset_by_id) | **DELETE** /assets/{asset-id} | Delete an asset
[**delete_bulk_assets**](AssetsApi.md#delete_bulk_assets) | **DELETE** /assets-bulk | Delete a list of assets
[**dry_run_delete_bulk_assets**](AssetsApi.md#dry_run_delete_bulk_assets) | **DELETE** /assets-bulk/dry-run | Dry-run for deleting a list of assets
[**dry_run_post_bulk_assets**](AssetsApi.md#dry_run_post_bulk_assets) | **POST** /assets-bulk/dry-run | Dry-run for creating a list of assets
[**dry_run_put_bulk_assets**](AssetsApi.md#dry_run_put_bulk_assets) | **PUT** /assets-bulk/dry-run | Dry-run for creating or updating a list of assets
[**get_asset_by_id**](AssetsApi.md#get_asset_by_id) | **GET** /assets/{asset-id} | Information about an asset
[**get_assets**](AssetsApi.md#get_assets) | **GET** /assets | Information about assets
[**get_attribute_display**](AssetsApi.md#get_attribute_display) | **GET** /attribute-display | How attributes are displayed
[**post_asset**](AssetsApi.md#post_asset) | **POST** /assets | Create an asset
[**post_bulk_assets**](AssetsApi.md#post_bulk_assets) | **POST** /assets-bulk | Create a list of assets
[**put_asset**](AssetsApi.md#put_asset) | **PUT** /assets | Create or update an asset
[**put_asset_by_id**](AssetsApi.md#put_asset_by_id) | **PUT** /assets/{asset-id} | Update an asset
[**put_attribute_display**](AssetsApi.md#put_attribute_display) | **PUT** /attribute-display | Create or update how attributes are displayed
[**put_bulk_assets**](AssetsApi.md#put_bulk_assets) | **PUT** /assets-bulk | Create or update a list of assets


# **delete_asset_by_id**
> delete_asset_by_id(asset_id)

Delete an asset

Deletes an asset

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = 4711 # int | The id of the asset

    # example passing only required values which don't have defaults set
    try:
        # Delete an asset
        api_instance.delete_asset_by_id(asset_id)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->delete_asset_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted the asset |  -  |
**404** | Asset type with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_assets**
> delete_bulk_assets(request_body)

Delete a list of assets

Delete multiple assets based on the identifiers defined by the 'identifyBy' parameter.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.str_none_type import StrNoneType
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    request_body = [
        "1234",
    ] # [str] | 
    identify_by = "resourceId" # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a list of assets
        api_instance.delete_bulk_assets(request_body)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->delete_bulk_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a list of assets
        api_instance.delete_bulk_assets(request_body, identify_by=identify_by, expansions=expansions)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->delete_bulk_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**|  |
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The complete list of assets have been successfully deleted. |  -  |
**422** | Issues may arise during the deletion process. If at least one asset encounters an error and cannot be deleted or is not found, no changes will be applied to any of the assets in the list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_delete_bulk_assets**
> [AssetDryRun] dry_run_delete_bulk_assets(request_body)

Dry-run for deleting a list of assets

Simulates the process of deleting multiple assets via the 'DELETE /assets-bulk' without actually persisting any changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset_dry_run import AssetDryRun
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    request_body = [
        "1234",
    ] # [str] | 
    identify_by = "resourceId" # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Dry-run for deleting a list of assets
        api_response = api_instance.dry_run_delete_bulk_assets(request_body)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->dry_run_delete_bulk_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Dry-run for deleting a list of assets
        api_response = api_instance.dry_run_delete_bulk_assets(request_body, identify_by=identify_by, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->dry_run_delete_bulk_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**|  |
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[AssetDryRun]**](AssetDryRun.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of expected results if the request is actually performed. The content displays the list of expected results in the same order as the initial request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_post_bulk_assets**
> [AssetDryRun] dry_run_post_bulk_assets(asset)

Dry-run for creating a list of assets

Simulates the process of creating assets via the 'POST /assets-bulk' endpoint without actually persisting any changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from eliona.api_client.model.asset_dry_run import AssetDryRun
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset = [
        Asset(
            resource_id="123e4567-e89b-12d3-a456-426655440000",
            device_ids=["XYZ0123",173493272],
            project_id="99",
            global_asset_identifier="zurich_swiss",
            name="Station Zurich",
            asset_type="asset_type_example",
            latitude=47.3667,
            longitude=8.55,
            is_tracker=False,
            description="Weather station Zurich, Swiss",
            parent_functional_asset_id=4712,
            parent_locational_asset_id=4712,
            tags=["weather","location"],
            attachments=[
                Attachment(
                    name="example.gif",
                    content_type="image/png",
                    encoding="base64",
                    content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                ),
            ],
        ),
    ] # [Asset] | 
    identify_by = "resourceId" # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Dry-run for creating a list of assets
        api_response = api_instance.dry_run_post_bulk_assets(asset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->dry_run_post_bulk_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Dry-run for creating a list of assets
        api_response = api_instance.dry_run_post_bulk_assets(asset, identify_by=identify_by, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->dry_run_post_bulk_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**[Asset]**](Asset.md)|  |
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[AssetDryRun]**](AssetDryRun.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of expected results if the request is actually performed. The content displays the list of expected results in the same order as the initial request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_put_bulk_assets**
> [AssetDryRun] dry_run_put_bulk_assets(asset)

Dry-run for creating or updating a list of assets

Simulates the process of creating or updating assets via the 'PUT /assets-bulk' endpoint without actually persisting any changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from eliona.api_client.model.asset_dry_run import AssetDryRun
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset = [
        Asset(
            resource_id="123e4567-e89b-12d3-a456-426655440000",
            device_ids=["XYZ0123",173493272],
            project_id="99",
            global_asset_identifier="zurich_swiss",
            name="Station Zurich",
            asset_type="asset_type_example",
            latitude=47.3667,
            longitude=8.55,
            is_tracker=False,
            description="Weather station Zurich, Swiss",
            parent_functional_asset_id=4712,
            parent_locational_asset_id=4712,
            tags=["weather","location"],
            attachments=[
                Attachment(
                    name="example.gif",
                    content_type="image/png",
                    encoding="base64",
                    content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                ),
            ],
        ),
    ] # [Asset] | 
    identify_by = "resourceId" # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Dry-run for creating or updating a list of assets
        api_response = api_instance.dry_run_put_bulk_assets(asset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->dry_run_put_bulk_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Dry-run for creating or updating a list of assets
        api_response = api_instance.dry_run_put_bulk_assets(asset, identify_by=identify_by, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->dry_run_put_bulk_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**[Asset]**](Asset.md)|  |
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[AssetDryRun]**](AssetDryRun.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of expected results if the request is actually performed. The content displays the list of expected results in the same order as the initial request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> Asset get_asset_by_id(asset_id)

Information about an asset

Gets information about an asset.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = 4711 # int | The id of the asset
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

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
        api_response = api_instance.get_asset_by_id(asset_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->get_asset_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**Asset**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset_type_name = "weather_location" # str | Filter the name of the asset type (optional)
    project_id = "projectId_example" # str, none_type | Filter for a specific project (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about assets
        api_response = api_instance.get_assets(asset_type_name=asset_type_name, project_id=project_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->get_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| Filter the name of the asset type | [optional]
 **project_id** | **str, none_type**| Filter for a specific project | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[Asset]**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_display**
> AttributeDisplay get_attribute_display()

How attributes are displayed

Gets information about how attributes for specific assets are displayed in frontend.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.attribute_display import AttributeDisplay
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # How attributes are displayed
        api_response = api_instance.get_attribute_display()
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->get_attribute_display: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AttributeDisplay**](AttributeDisplay.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned display information for attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset**
> Asset post_asset(asset)

Create an asset

This process involves creating an asset. The determination if the asset already exists and cannot be created is done by the 'identifyBy' parameter, which specifies the field used for identification. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from eliona.api_client.model.str_none_type import StrNoneType
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset = Asset(
        resource_id="123e4567-e89b-12d3-a456-426655440000",
        device_ids=["XYZ0123",173493272],
        project_id="99",
        global_asset_identifier="zurich_swiss",
        name="Station Zurich",
        asset_type="asset_type_example",
        latitude=47.3667,
        longitude=8.55,
        is_tracker=False,
        description="Weather station Zurich, Swiss",
        parent_functional_asset_id=4712,
        parent_locational_asset_id=4712,
        tags=["weather","location"],
        attachments=[
            Attachment(
                name="example.gif",
                content_type="image/png",
                encoding="base64",
                content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
            ),
        ],
    ) # Asset | 
    identify_by = "resourceId" # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an asset
        api_response = api_instance.post_asset(asset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->post_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an asset
        api_response = api_instance.post_asset(asset, identify_by=identify_by, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->post_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**Asset**](Asset.md)|  |
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**Asset**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new asset  |  -  |
**422** | Issues arisen during the creation or updating process.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bulk_assets**
> [Asset] post_bulk_assets(asset)

Create a list of assets

This process involves creating the assets in the list. The determination if the asset already exists and cannot be created is done by the 'identifyBy' parameter, which specifies the field used for identification.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from eliona.api_client.model.str_none_type import StrNoneType
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset = [
        Asset(
            resource_id="123e4567-e89b-12d3-a456-426655440000",
            device_ids=["XYZ0123",173493272],
            project_id="99",
            global_asset_identifier="zurich_swiss",
            name="Station Zurich",
            asset_type="asset_type_example",
            latitude=47.3667,
            longitude=8.55,
            is_tracker=False,
            description="Weather station Zurich, Swiss",
            parent_functional_asset_id=4712,
            parent_locational_asset_id=4712,
            tags=["weather","location"],
            attachments=[
                Attachment(
                    name="example.gif",
                    content_type="image/png",
                    encoding="base64",
                    content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                ),
            ],
        ),
    ] # [Asset] | 
    identify_by = "resourceId" # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a list of assets
        api_response = api_instance.post_bulk_assets(asset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->post_bulk_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a list of assets
        api_response = api_instance.post_bulk_assets(asset, identify_by=identify_by, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->post_bulk_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**[Asset]**](Asset.md)|  |
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[Asset]**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The complete list of assets has been successfully created. The content displays the list of assets in the same order as the initial request, along with some generated or default values (e.g. timestamps, IDs). |  -  |
**422** | Issues may arise during the creation process when handling the assets in the list. In such cases, if at least one asset encounters an error and cannot be created, no changes will be applied to any of the assets in the list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset**
> Asset put_asset(asset)

Create or update an asset

This process involves creating or updating an asset. The choice between updating or creating is determined by the 'identifyBy' parameter, which specifies the field used for identification. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from eliona.api_client.model.str_none_type import StrNoneType
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset = Asset(
        resource_id="123e4567-e89b-12d3-a456-426655440000",
        device_ids=["XYZ0123",173493272],
        project_id="99",
        global_asset_identifier="zurich_swiss",
        name="Station Zurich",
        asset_type="asset_type_example",
        latitude=47.3667,
        longitude=8.55,
        is_tracker=False,
        description="Weather station Zurich, Swiss",
        parent_functional_asset_id=4712,
        parent_locational_asset_id=4712,
        tags=["weather","location"],
        attachments=[
            Attachment(
                name="example.gif",
                content_type="image/png",
                encoding="base64",
                content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
            ),
        ],
    ) # Asset | 
    identify_by = "resourceId" # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update an asset
        api_response = api_instance.put_asset(asset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->put_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update an asset
        api_response = api_instance.put_asset(asset, identify_by=identify_by, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->put_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**Asset**](Asset.md)|  |
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**Asset**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing asset |  -  |
**422** | Issues arisen during the creation or updating process. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_by_id**
> Asset put_asset_by_id(asset_id, asset)

Update an asset

Deprecated: use the 'PUT /asset' method and optionally the 'identifyBy' parameter to update a specific asset. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset_id = 4711 # int | The id of the asset
    asset = Asset(
        resource_id="123e4567-e89b-12d3-a456-426655440000",
        device_ids=["XYZ0123",173493272],
        project_id="99",
        global_asset_identifier="zurich_swiss",
        name="Station Zurich",
        asset_type="asset_type_example",
        latitude=47.3667,
        longitude=8.55,
        is_tracker=False,
        description="Weather station Zurich, Swiss",
        parent_functional_asset_id=4712,
        parent_locational_asset_id=4712,
        tags=["weather","location"],
        attachments=[
            Attachment(
                name="example.gif",
                content_type="image/png",
                encoding="base64",
                content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
            ),
        ],
    ) # Asset | 
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an asset
        api_response = api_instance.put_asset_by_id(asset_id, asset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->put_asset_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an asset
        api_response = api_instance.put_asset_by_id(asset_id, asset, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->put_asset_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset |
 **asset** | [**Asset**](Asset.md)|  |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**Asset**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing asset |  -  |
**404** | Asset with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_attribute_display**
> AttributeDisplay put_attribute_display(attribute_display)

Create or update how attributes are displayed

Create or update how attributes are displayed in frontend. Uses the unique combination of asset id, subtype and attribute name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.attribute_display import AttributeDisplay
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    attribute_display = AttributeDisplay(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        unit="°C",
        precision=1,
        min=3.14,
        max=3.14,
        viewer=False,
        ar=False,
        sequence=1,
        map=[
            ValueMapping(
                value=5,
                text="five",
            ),
        ],
    ) # AttributeDisplay | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update how attributes are displayed
        api_response = api_instance.put_attribute_display(attribute_display)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->put_attribute_display: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_display** | [**AttributeDisplay**](AttributeDisplay.md)|  |

### Return type

[**AttributeDisplay**](AttributeDisplay.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated or created display information for attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bulk_assets**
> [Asset] put_bulk_assets(asset)

Create or update a list of assets

This process involves creating or updating assets. The choice between updating or creating an asset is determined by the 'identifyBy' parameter, which specifies the field used for identification.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import assets_api
from eliona.api_client.model.asset import Asset
from eliona.api_client.model.str_none_type import StrNoneType
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    asset = [
        Asset(
            resource_id="123e4567-e89b-12d3-a456-426655440000",
            device_ids=["XYZ0123",173493272],
            project_id="99",
            global_asset_identifier="zurich_swiss",
            name="Station Zurich",
            asset_type="asset_type_example",
            latitude=47.3667,
            longitude=8.55,
            is_tracker=False,
            description="Weather station Zurich, Swiss",
            parent_functional_asset_id=4712,
            parent_locational_asset_id=4712,
            tags=["weather","location"],
            attachments=[
                Attachment(
                    name="example.gif",
                    content_type="image/png",
                    encoding="base64",
                    content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                ),
            ],
        ),
    ] # [Asset] | 
    identify_by = "resourceId" # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update a list of assets
        api_response = api_instance.put_bulk_assets(asset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->put_bulk_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update a list of assets
        api_response = api_instance.put_bulk_assets(asset, identify_by=identify_by, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetsApi->put_bulk_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**[Asset]**](Asset.md)|  |
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[Asset]**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The complete list of assets has been successfully created or updated. The content displays the list of assets in the same order as the initial request, along with some generated or default values (e.g. timestamps, IDs). |  -  |
**422** | Issues may arise during the creation or updating process when handling the assets in the list. In such cases, if at least one asset encounters an error and cannot be created or updated, no changes will be applied to any of the assets in the list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


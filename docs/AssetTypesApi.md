# eliona.api_client.AssetTypesApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset_type_by_name**](AssetTypesApi.md#delete_asset_type_by_name) | **DELETE** /asset-types/{asset-type-name} | Delete an asset type
[**get_asset_type_by_name**](AssetTypesApi.md#get_asset_type_by_name) | **GET** /asset-types/{asset-type-name} | Information about an asset type
[**get_asset_types**](AssetTypesApi.md#get_asset_types) | **GET** /asset-types | List of asset types
[**put_asset_type**](AssetTypesApi.md#put_asset_type) | **PUT** /asset-types | Create or update an asset type
[**put_asset_type_attribute**](AssetTypesApi.md#put_asset_type_attribute) | **PUT** /asset-types/{asset-type-name}/attributes | Create or update an asset type attribute


# **delete_asset_type_by_name**
> delete_asset_type_by_name(asset_type_name)

Delete an asset type

Deletes an asset type and the attributes for this asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import asset_types_api
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asset_types_api.AssetTypesApi(api_client)
    asset_type_name = "weather_location" # str | The name of the asset type

    # example passing only required values which don't have defaults set
    try:
        # Delete an asset type
        api_instance.delete_asset_type_by_name(asset_type_name)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->delete_asset_type_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| The name of the asset type |

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
**204** | Successfully deleted the asset type |  -  |
**404** | Asset type with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_type_by_name**
> AssetType get_asset_type_by_name(asset_type_name)

Information about an asset type

Gets information about an asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import asset_types_api
from eliona.api_client.model.asset_type import AssetType
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asset_types_api.AssetTypesApi(api_client)
    asset_type_name = "weather_location" # str | The name of the asset type
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Information about an asset type
        api_response = api_instance.get_asset_type_by_name(asset_type_name)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->get_asset_type_by_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about an asset type
        api_response = api_instance.get_asset_type_by_name(asset_type_name, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->get_asset_type_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| The name of the asset type |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**AssetType**](AssetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an asset type by name. |  -  |
**404** | Asset type with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types**
> [AssetType] get_asset_types()

List of asset types

Returns a list of asset types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import asset_types_api
from eliona.api_client.model.asset_type import AssetType
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asset_types_api.AssetTypesApi(api_client)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of asset types
        api_response = api_instance.get_asset_types(expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->get_asset_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[AssetType]**](AssetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of asset types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_type**
> AssetType put_asset_type(asset_type)

Create or update an asset type

Create a new asset type or update an asset type if already exists

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import asset_types_api
from eliona.api_client.model.asset_type import AssetType
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asset_types_api.AssetTypesApi(api_client)
    asset_type = AssetType(
        name="weather_location",
        custom=True,
        vendor="vendor_example",
        model="model_example",
        translation=Translation(
            de="Das ist eine deutsche Beschreibung",
            en="This is an english description",
            fr="Ceci est une description français",
            it="Questa è una descrizione italiana",
        ),
        urldoc="urldoc_example",
        icon="weather",
        payload_function="PLS",
        allowed_inactivity="0 hours 5 mins",
        attributes=[
            AssetTypeAttribute(
                asset_type_name="weather_location",
                name="temperature",
                subtype=DataSubtype("input"),
                type="temperature",
                enable=True,
                translation=Translation(
                    de="Das ist eine deutsche Beschreibung",
                    en="This is an english description",
                    fr="Ceci est une description français",
                    it="Questa è una descrizione italiana",
                ),
                unit="°C",
                precision=1,
                min=3.14,
                max=3.14,
                aggregation_mode="avg",
                aggregation_rasters=[
                    "DAY",
                ],
                viewer=False,
                ar=False,
                sequence=1,
                virtual=True,
                scale=3.14,
                zero=3.14,
                map={},
                source_path=[
                    "source_path_example",
                ],
                is_digital=True,
            ),
        ],
    ) # AssetType | 
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update an asset type
        api_response = api_instance.put_asset_type(asset_type)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->put_asset_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update an asset type
        api_response = api_instance.put_asset_type(asset_type, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->put_asset_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type** | [**AssetType**](AssetType.md)|  |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**AssetType**](AssetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new or updated an existing asset type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_type_attribute**
> put_asset_type_attribute(asset_type_name, asset_type_attribute)

Create or update an asset type attribute

Create a new asset type attribute or update an asset type attribute if already exists

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import asset_types_api
from eliona.api_client.model.asset_type_attribute import AssetTypeAttribute
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asset_types_api.AssetTypesApi(api_client)
    asset_type_name = "weather_location" # str | The name of the asset type
    asset_type_attribute = AssetTypeAttribute(
        asset_type_name="weather_location",
        name="temperature",
        subtype=DataSubtype("input"),
        type="temperature",
        enable=True,
        translation=Translation(
            de="Das ist eine deutsche Beschreibung",
            en="This is an english description",
            fr="Ceci est une description français",
            it="Questa è una descrizione italiana",
        ),
        unit="°C",
        precision=1,
        min=3.14,
        max=3.14,
        aggregation_mode="avg",
        aggregation_rasters=[
            "DAY",
        ],
        viewer=False,
        ar=False,
        sequence=1,
        virtual=True,
        scale=3.14,
        zero=3.14,
        map={},
        source_path=[
            "source_path_example",
        ],
        is_digital=True,
    ) # AssetTypeAttribute | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an asset type attribute
        api_instance.put_asset_type_attribute(asset_type_name, asset_type_attribute)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->put_asset_type_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| The name of the asset type |
 **asset_type_attribute** | [**AssetTypeAttribute**](AssetTypeAttribute.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new or updated an existing asset type attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


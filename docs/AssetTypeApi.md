# eliona.api_client.AssetTypeApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_types**](AssetTypeApi.md#get_asset_types) | **GET** /asset-type | List of asset types
[**post_asset_type**](AssetTypeApi.md#post_asset_type) | **POST** /asset-type | Create or update an asset type
[**post_asset_type_attribute**](AssetTypeApi.md#post_asset_type_attribute) | **POST** /asset-type-attribute | Create or update an asset type attribute


# **get_asset_types**
> [AssetType] get_asset_types()

List of asset types

Returns a list of asset types

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import asset_type_api
from eliona.api_client.model.asset_type import AssetType
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = asset_type_api.AssetTypeApi(api_client)
    limit = 20 # int | Limits the number of items on a page (optional)
    offset = 1 # int | Specifies the page number to be displayed (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of asset types
        api_response = api_instance.get_asset_types(limit=limit, offset=offset)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypeApi->get_asset_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of items on a page | [optional]
 **offset** | **int**| Specifies the page number to be displayed | [optional]

### Return type

[**[AssetType]**](AssetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of asset types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset_type**
> post_asset_type(asset_type)

Create or update an asset type

Create a new asset type or update an asset type if already exists

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import asset_type_api
from eliona.api_client.model.asset_type import AssetType
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = asset_type_api.AssetTypeApi(api_client)
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
        attributes=[
            Attribute(
                asset_type_name="weather_location",
                name="temperature",
                subtype=HeapSubtype("input"),
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
                pipeline=AttributePipeline(
                    mode="avg",
                    raster=[
                        "S1",
                    ],
                ),
                viewer=False,
                ar=False,
                sequence=1,
                virtual=True,
            ),
        ],
    ) # AssetType | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an asset type
        api_instance.post_asset_type(asset_type)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypeApi->post_asset_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type** | [**AssetType**](AssetType.md)|  |

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
**200** | Successfully created a new or updated an existing asset type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset_type_attribute**
> post_asset_type_attribute(attribute)

Create or update an asset type attribute

Create a new asset type attribute or update an asset type attribute if already exists

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import asset_type_api
from eliona.api_client.model.attribute import Attribute
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = asset_type_api.AssetTypeApi(api_client)
    attribute = Attribute(
        asset_type_name="weather_location",
        name="temperature",
        subtype=HeapSubtype("input"),
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
        pipeline=AttributePipeline(
            mode="avg",
            raster=[
                "S1",
            ],
        ),
        viewer=False,
        ar=False,
        sequence=1,
        virtual=True,
    ) # Attribute | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an asset type attribute
        api_instance.post_asset_type_attribute(attribute)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypeApi->post_asset_type_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute** | [**Attribute**](Attribute.md)|  |

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
**200** | Successfully created a new or updated an existing asset type attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


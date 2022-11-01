<a name="__pageTop"></a>
# eliona.api_client.apis.tags.asset_types_api.AssetTypesApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset_type_by_name**](#delete_asset_type_by_name) | **delete** /asset-types/{asset-type-name} | Delete an asset type
[**get_asset_type_by_name**](#get_asset_type_by_name) | **get** /asset-types/{asset-type-name} | Information about an asset type
[**get_asset_types**](#get_asset_types) | **get** /asset-types | List of asset types
[**post_asset_type**](#post_asset_type) | **post** /asset-types | Create an asset type
[**post_asset_type_attribute**](#post_asset_type_attribute) | **post** /asset-types/{asset-type-name}/attributes | Create asset type attribute
[**put_asset_type**](#put_asset_type) | **put** /asset-types | Create or update an asset type
[**put_asset_type_attribute**](#put_asset_type_attribute) | **put** /asset-types/{asset-type-name}/attributes | Create or update an asset type attribute
[**put_asset_type_by_name**](#put_asset_type_by_name) | **put** /asset-types/{asset-type-name} | Update an asset type

# **delete_asset_type_by_name**
<a name="delete_asset_type_by_name"></a>
> delete_asset_type_by_name(asset_type_name)

Delete an asset type

Deletes an asset type and the attributes for this asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import asset_types_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'asset-type-name': "weather_location",
    }
    try:
        # Delete an asset type
        api_response = api_instance.delete_asset_type_by_name(
            path_params=path_params,
        )
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->delete_asset_type_by_name: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asset-type-name | AssetTypeNameSchema | | 

# AssetTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_asset_type_by_name.ApiResponseFor204) | Successfully deleted the asset type
404 | [ApiResponseFor404](#delete_asset_type_by_name.ApiResponseFor404) | Asset type with name not found

#### delete_asset_type_by_name.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_asset_type_by_name.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_asset_type_by_name**
<a name="get_asset_type_by_name"></a>
> AssetType get_asset_type_by_name(asset_type_name)

Information about an asset type

Gets information about an asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import asset_types_api
from eliona/api_client.model.asset_type import AssetType
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

    # example passing only required values which don't have defaults set
    path_params = {
        'asset-type-name': "weather_location",
    }
    query_params = {
    }
    try:
        # Information about an asset type
        api_response = api_instance.get_asset_type_by_name(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->get_asset_type_by_name: %s\n" % e)

    # example passing only optional values
    path_params = {
        'asset-type-name': "weather_location",
    }
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    try:
        # Information about an asset type
        api_response = api_instance.get_asset_type_by_name(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->get_asset_type_by_name: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
expansions | ExpansionsSchema | | optional


# ExpansionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asset-type-name | AssetTypeNameSchema | | 

# AssetTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_asset_type_by_name.ApiResponseFor200) | Successfully returned an asset type by name.
404 | [ApiResponseFor404](#get_asset_type_by_name.ApiResponseFor404) | Asset type with name not found

#### get_asset_type_by_name.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetType**](../../models/AssetType.md) |  | 


#### get_asset_type_by_name.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_asset_types**
<a name="get_asset_types"></a>
> [AssetType] get_asset_types()

List of asset types

Returns a list of asset types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import asset_types_api
from eliona/api_client.model.asset_type import AssetType
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

    # example passing only optional values
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    try:
        # List of asset types
        api_response = api_instance.get_asset_types(
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->get_asset_types: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
expansions | ExpansionsSchema | | optional


# ExpansionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_asset_types.ApiResponseFor200) | Successfully returned a list of asset types

#### get_asset_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AssetType**]({{complexTypePrefix}}AssetType.md) | [**AssetType**]({{complexTypePrefix}}AssetType.md) | [**AssetType**]({{complexTypePrefix}}AssetType.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_asset_type**
<a name="post_asset_type"></a>
> AssetType post_asset_type(asset_type)

Create an asset type

Create a new asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import asset_types_api
from eliona/api_client.model.asset_type import AssetType
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = AssetType(
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
                translation=Translation(),
                unit="°C",
                precision=1,
                min=3.14,
                max=3.14,
                aggregation_mode="avg",
                aggregation_rasters=[
                    "DAY"
                ],
                viewer=False,
                ar=False,
                sequence=1,
                virtual=True,
                scale=3.14,
                zero=3.14,
                map=dict(),
                source_path=[
                    "source_path_example"
                ],
                is_digital=True,
            )
        ],
    )
    try:
        # Create an asset type
        api_response = api_instance.post_asset_type(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->post_asset_type: %s\n" % e)

    # example passing only optional values
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    body = AssetType(
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
                translation=Translation(),
                unit="°C",
                precision=1,
                min=3.14,
                max=3.14,
                aggregation_mode="avg",
                aggregation_rasters=[
                    "DAY"
                ],
                viewer=False,
                ar=False,
                sequence=1,
                virtual=True,
                scale=3.14,
                zero=3.14,
                map=dict(),
                source_path=[
                    "source_path_example"
                ],
                is_digital=True,
            )
        ],
    )
    try:
        # Create an asset type
        api_response = api_instance.post_asset_type(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->post_asset_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetType**](../../models/AssetType.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
expansions | ExpansionsSchema | | optional


# ExpansionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_asset_type.ApiResponseFor201) | Successfully created a new asset type
409 | [ApiResponseFor409](#post_asset_type.ApiResponseFor409) | Asset type name already exists

#### post_asset_type.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetType**](../../models/AssetType.md) |  | 


#### post_asset_type.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_asset_type_attribute**
<a name="post_asset_type_attribute"></a>
> AssetTypeAttribute post_asset_type_attribute(asset_type_nameasset_type_attribute)

Create asset type attribute

Create a new asset type attribute.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import asset_types_api
from eliona/api_client.model.asset_type_attribute import AssetTypeAttribute
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

    # example passing only required values which don't have defaults set
    path_params = {
        'asset-type-name': "weather_location",
    }
    body = AssetTypeAttribute(
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
            "DAY"
        ],
        viewer=False,
        ar=False,
        sequence=1,
        virtual=True,
        scale=3.14,
        zero=3.14,
        map=dict(),
        source_path=[
            "source_path_example"
        ],
        is_digital=True,
    )
    try:
        # Create asset type attribute
        api_response = api_instance.post_asset_type_attribute(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->post_asset_type_attribute: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetTypeAttribute**](../../models/AssetTypeAttribute.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asset-type-name | AssetTypeNameSchema | | 

# AssetTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_asset_type_attribute.ApiResponseFor201) | Successfully created a new asset type attribute
409 | [ApiResponseFor409](#post_asset_type_attribute.ApiResponseFor409) | Combination of asset type name, subtype and attribute name already exists

#### post_asset_type_attribute.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetTypeAttribute**](../../models/AssetTypeAttribute.md) |  | 


#### post_asset_type_attribute.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_asset_type**
<a name="put_asset_type"></a>
> AssetType put_asset_type(asset_type)

Create or update an asset type

Create a new asset type or update an asset type if already exists. Uses the unique asset type name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import asset_types_api
from eliona/api_client.model.asset_type import AssetType
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = AssetType(
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
                translation=Translation(),
                unit="°C",
                precision=1,
                min=3.14,
                max=3.14,
                aggregation_mode="avg",
                aggregation_rasters=[
                    "DAY"
                ],
                viewer=False,
                ar=False,
                sequence=1,
                virtual=True,
                scale=3.14,
                zero=3.14,
                map=dict(),
                source_path=[
                    "source_path_example"
                ],
                is_digital=True,
            )
        ],
    )
    try:
        # Create or update an asset type
        api_response = api_instance.put_asset_type(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->put_asset_type: %s\n" % e)

    # example passing only optional values
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    body = AssetType(
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
                translation=Translation(),
                unit="°C",
                precision=1,
                min=3.14,
                max=3.14,
                aggregation_mode="avg",
                aggregation_rasters=[
                    "DAY"
                ],
                viewer=False,
                ar=False,
                sequence=1,
                virtual=True,
                scale=3.14,
                zero=3.14,
                map=dict(),
                source_path=[
                    "source_path_example"
                ],
                is_digital=True,
            )
        ],
    )
    try:
        # Create or update an asset type
        api_response = api_instance.put_asset_type(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->put_asset_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetType**](../../models/AssetType.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
expansions | ExpansionsSchema | | optional


# ExpansionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_asset_type.ApiResponseFor200) | Successfully created a new or updated an existing asset type

#### put_asset_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetType**](../../models/AssetType.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_asset_type_attribute**
<a name="put_asset_type_attribute"></a>
> AssetTypeAttribute put_asset_type_attribute(asset_type_nameasset_type_attribute)

Create or update an asset type attribute

Create a new asset type attribute or update an asset type attribute if already exists. Uses the unique combination of asset type name, subtype and attribute name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import asset_types_api
from eliona/api_client.model.asset_type_attribute import AssetTypeAttribute
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

    # example passing only required values which don't have defaults set
    path_params = {
        'asset-type-name': "weather_location",
    }
    body = AssetTypeAttribute(
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
            "DAY"
        ],
        viewer=False,
        ar=False,
        sequence=1,
        virtual=True,
        scale=3.14,
        zero=3.14,
        map=dict(),
        source_path=[
            "source_path_example"
        ],
        is_digital=True,
    )
    try:
        # Create or update an asset type attribute
        api_response = api_instance.put_asset_type_attribute(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->put_asset_type_attribute: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetTypeAttribute**](../../models/AssetTypeAttribute.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asset-type-name | AssetTypeNameSchema | | 

# AssetTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_asset_type_attribute.ApiResponseFor200) | Successfully created a new or updated an existing asset type attribute

#### put_asset_type_attribute.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetTypeAttribute**](../../models/AssetTypeAttribute.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_asset_type_by_name**
<a name="put_asset_type_by_name"></a>
> AssetType put_asset_type_by_name(asset_type_nameasset_type)

Update an asset type

Update an asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import asset_types_api
from eliona/api_client.model.asset_type import AssetType
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

    # example passing only required values which don't have defaults set
    path_params = {
        'asset-type-name': "weather_location",
    }
    query_params = {
    }
    body = AssetType(
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
                translation=Translation(),
                unit="°C",
                precision=1,
                min=3.14,
                max=3.14,
                aggregation_mode="avg",
                aggregation_rasters=[
                    "DAY"
                ],
                viewer=False,
                ar=False,
                sequence=1,
                virtual=True,
                scale=3.14,
                zero=3.14,
                map=dict(),
                source_path=[
                    "source_path_example"
                ],
                is_digital=True,
            )
        ],
    )
    try:
        # Update an asset type
        api_response = api_instance.put_asset_type_by_name(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->put_asset_type_by_name: %s\n" % e)

    # example passing only optional values
    path_params = {
        'asset-type-name': "weather_location",
    }
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    body = AssetType(
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
                translation=Translation(),
                unit="°C",
                precision=1,
                min=3.14,
                max=3.14,
                aggregation_mode="avg",
                aggregation_rasters=[
                    "DAY"
                ],
                viewer=False,
                ar=False,
                sequence=1,
                virtual=True,
                scale=3.14,
                zero=3.14,
                map=dict(),
                source_path=[
                    "source_path_example"
                ],
                is_digital=True,
            )
        ],
    )
    try:
        # Update an asset type
        api_response = api_instance.put_asset_type_by_name(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AssetTypesApi->put_asset_type_by_name: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetType**](../../models/AssetType.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
expansions | ExpansionsSchema | | optional


# ExpansionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asset-type-name | AssetTypeNameSchema | | 

# AssetTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_asset_type_by_name.ApiResponseFor200) | Successfully updated an existing asset type
404 | [ApiResponseFor404](#put_asset_type_by_name.ApiResponseFor404) | Asset type with name not found

#### put_asset_type_by_name.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetType**](../../models/AssetType.md) |  | 


#### put_asset_type_by_name.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


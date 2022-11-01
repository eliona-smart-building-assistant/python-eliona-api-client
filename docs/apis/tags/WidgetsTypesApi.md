<a name="__pageTop"></a>
# eliona.api_client.apis.tags.widgets_types_api.WidgetsTypesApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_widget_type_by_name**](#delete_widget_type_by_name) | **delete** /widget-types/{widget-type-name} | Delete a widget type
[**get_widget_type_by_name**](#get_widget_type_by_name) | **get** /widget-types/{widget-type-name} | Information about a widget type
[**get_widget_types**](#get_widget_types) | **get** /widget-types | List of widget types
[**post_widget_type**](#post_widget_type) | **post** /widget-types | Create a widget type
[**put_widget_type**](#put_widget_type) | **put** /widget-types | Create or update a widget type
[**put_widget_type_by_name**](#put_widget_type_by_name) | **put** /widget-types/{widget-type-name} | Update a widget type

# **delete_widget_type_by_name**
<a name="delete_widget_type_by_name"></a>
> delete_widget_type_by_name(widget_type_name)

Delete a widget type

Deletes a widget type and the elements for this widget type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import widgets_types_api
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
    api_instance = widgets_types_api.WidgetsTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'widget-type-name': "weather",
    }
    try:
        # Delete a widget type
        api_response = api_instance.delete_widget_type_by_name(
            path_params=path_params,
        )
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->delete_widget_type_by_name: %s\n" % e)
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
widget-type-name | WidgetTypeNameSchema | | 

# WidgetTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_widget_type_by_name.ApiResponseFor204) | Successfully deleted the widget type
404 | [ApiResponseFor404](#delete_widget_type_by_name.ApiResponseFor404) | Widget type with name not found

#### delete_widget_type_by_name.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_widget_type_by_name.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_widget_type_by_name**
<a name="get_widget_type_by_name"></a>
> WidgetType get_widget_type_by_name(widget_type_name)

Information about a widget type

Gets information about a widget type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import widgets_types_api
from eliona/api_client.model.widget_type import WidgetType
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
    api_instance = widgets_types_api.WidgetsTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'widget-type-name': "weather",
    }
    query_params = {
    }
    try:
        # Information about a widget type
        api_response = api_instance.get_widget_type_by_name(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->get_widget_type_by_name: %s\n" % e)

    # example passing only optional values
    path_params = {
        'widget-type-name': "weather",
    }
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    try:
        # Information about a widget type
        api_response = api_instance.get_widget_type_by_name(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->get_widget_type_by_name: %s\n" % e)
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
widget-type-name | WidgetTypeNameSchema | | 

# WidgetTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_widget_type_by_name.ApiResponseFor200) | Successfully returned a widget type by name.
404 | [ApiResponseFor404](#get_widget_type_by_name.ApiResponseFor404) | Widget type with name not found

#### get_widget_type_by_name.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WidgetType**](../../models/WidgetType.md) |  | 


#### get_widget_type_by_name.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_widget_types**
<a name="get_widget_types"></a>
> [WidgetType] get_widget_types()

List of widget types

Returns a list of widget types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import widgets_types_api
from eliona/api_client.model.widget_type import WidgetType
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
    api_instance = widgets_types_api.WidgetsTypesApi(api_client)

    # example passing only optional values
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    try:
        # List of widget types
        api_response = api_instance.get_widget_types(
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->get_widget_types: %s\n" % e)
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
200 | [ApiResponseFor200](#get_widget_types.ApiResponseFor200) | Successfully returned a list of widget types

#### get_widget_types.ApiResponseFor200
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
[**WidgetType**]({{complexTypePrefix}}WidgetType.md) | [**WidgetType**]({{complexTypePrefix}}WidgetType.md) | [**WidgetType**]({{complexTypePrefix}}WidgetType.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_widget_type**
<a name="post_widget_type"></a>
> WidgetType post_widget_type(widget_type)

Create a widget type

Create a new widget type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import widgets_types_api
from eliona/api_client.model.widget_type import WidgetType
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
    api_instance = widgets_types_api.WidgetsTypesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = WidgetType(
        id=4711,
        name="weather",
        custom=True,
        translation=Translation(
            de="Das ist eine deutsche Beschreibung",
            en="This is an english description",
            fr="Ceci est une description français",
            it="Questa è una descrizione italiana",
        ),
        icon="weather",
        with_alarm=False,
        with_timespan=False,
        elements=[
            WidgetTypeElement(
                id=4711,
                category="weather",
                sequence=1,
                config=dict(),
            )
        ],
    )
    try:
        # Create a widget type
        api_response = api_instance.post_widget_type(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->post_widget_type: %s\n" % e)

    # example passing only optional values
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    body = WidgetType(
        id=4711,
        name="weather",
        custom=True,
        translation=Translation(
            de="Das ist eine deutsche Beschreibung",
            en="This is an english description",
            fr="Ceci est une description français",
            it="Questa è una descrizione italiana",
        ),
        icon="weather",
        with_alarm=False,
        with_timespan=False,
        elements=[
            WidgetTypeElement(
                id=4711,
                category="weather",
                sequence=1,
                config=dict(),
            )
        ],
    )
    try:
        # Create a widget type
        api_response = api_instance.post_widget_type(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->post_widget_type: %s\n" % e)
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
[**WidgetType**](../../models/WidgetType.md) |  | 


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
201 | [ApiResponseFor201](#post_widget_type.ApiResponseFor201) | Successfully created widget type
409 | [ApiResponseFor409](#post_widget_type.ApiResponseFor409) | Widget type name already exists

#### post_widget_type.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WidgetType**](../../models/WidgetType.md) |  | 


#### post_widget_type.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_widget_type**
<a name="put_widget_type"></a>
> WidgetType put_widget_type(widget_type)

Create or update a widget type

Create a new widget type or update it if already exists. Uses the unique widget type name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import widgets_types_api
from eliona/api_client.model.widget_type import WidgetType
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
    api_instance = widgets_types_api.WidgetsTypesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = WidgetType(
        id=4711,
        name="weather",
        custom=True,
        translation=Translation(
            de="Das ist eine deutsche Beschreibung",
            en="This is an english description",
            fr="Ceci est une description français",
            it="Questa è una descrizione italiana",
        ),
        icon="weather",
        with_alarm=False,
        with_timespan=False,
        elements=[
            WidgetTypeElement(
                id=4711,
                category="weather",
                sequence=1,
                config=dict(),
            )
        ],
    )
    try:
        # Create or update a widget type
        api_response = api_instance.put_widget_type(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->put_widget_type: %s\n" % e)

    # example passing only optional values
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    body = WidgetType(
        id=4711,
        name="weather",
        custom=True,
        translation=Translation(
            de="Das ist eine deutsche Beschreibung",
            en="This is an english description",
            fr="Ceci est une description français",
            it="Questa è una descrizione italiana",
        ),
        icon="weather",
        with_alarm=False,
        with_timespan=False,
        elements=[
            WidgetTypeElement(
                id=4711,
                category="weather",
                sequence=1,
                config=dict(),
            )
        ],
    )
    try:
        # Create or update a widget type
        api_response = api_instance.put_widget_type(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->put_widget_type: %s\n" % e)
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
[**WidgetType**](../../models/WidgetType.md) |  | 


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
200 | [ApiResponseFor200](#put_widget_type.ApiResponseFor200) | Successfully added or updated widget type

#### put_widget_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WidgetType**](../../models/WidgetType.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_widget_type_by_name**
<a name="put_widget_type_by_name"></a>
> WidgetType put_widget_type_by_name(widget_type_namewidget_type)

Update a widget type

Update a widget type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import widgets_types_api
from eliona/api_client.model.widget_type import WidgetType
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
    api_instance = widgets_types_api.WidgetsTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'widget-type-name': "weather",
    }
    query_params = {
    }
    body = WidgetType(
        id=4711,
        name="weather",
        custom=True,
        translation=Translation(
            de="Das ist eine deutsche Beschreibung",
            en="This is an english description",
            fr="Ceci est une description français",
            it="Questa è una descrizione italiana",
        ),
        icon="weather",
        with_alarm=False,
        with_timespan=False,
        elements=[
            WidgetTypeElement(
                id=4711,
                category="weather",
                sequence=1,
                config=dict(),
            )
        ],
    )
    try:
        # Update a widget type
        api_response = api_instance.put_widget_type_by_name(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->put_widget_type_by_name: %s\n" % e)

    # example passing only optional values
    path_params = {
        'widget-type-name': "weather",
    }
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    body = WidgetType(
        id=4711,
        name="weather",
        custom=True,
        translation=Translation(
            de="Das ist eine deutsche Beschreibung",
            en="This is an english description",
            fr="Ceci est une description français",
            it="Questa è una descrizione italiana",
        ),
        icon="weather",
        with_alarm=False,
        with_timespan=False,
        elements=[
            WidgetTypeElement(
                id=4711,
                category="weather",
                sequence=1,
                config=dict(),
            )
        ],
    )
    try:
        # Update a widget type
        api_response = api_instance.put_widget_type_by_name(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsTypesApi->put_widget_type_by_name: %s\n" % e)
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
[**WidgetType**](../../models/WidgetType.md) |  | 


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
widget-type-name | WidgetTypeNameSchema | | 

# WidgetTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_widget_type_by_name.ApiResponseFor200) | Successfully updated widget type
404 | [ApiResponseFor404](#put_widget_type_by_name.ApiResponseFor404) | Widget type with name not found

#### put_widget_type_by_name.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WidgetType**](../../models/WidgetType.md) |  | 


#### put_widget_type_by_name.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


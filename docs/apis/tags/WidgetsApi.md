<a name="__pageTop"></a>
# eliona.api_client.apis.tags.widgets_api.WidgetsApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_widgets**](#get_dashboard_widgets) | **get** /dashboards/{dashboard-id}/widgets | Information about widgets on dashboard
[**post_dashboard_widget**](#post_dashboard_widget) | **post** /dashboards/{dashboard-id}/widgets | Adds widget to dashboard

# **get_dashboard_widgets**
<a name="get_dashboard_widgets"></a>
> Widget get_dashboard_widgets(dashboard_id)

Information about widgets on dashboard

Gets information about widgets on a dashboard.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import widgets_api
from eliona/api_client.model.widget import Widget
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
    api_instance = widgets_api.WidgetsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dashboard-id': 4711,
    }
    query_params = {
    }
    try:
        # Information about widgets on dashboard
        api_response = api_instance.get_dashboard_widgets(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsApi->get_dashboard_widgets: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dashboard-id': 4711,
    }
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    try:
        # Information about widgets on dashboard
        api_response = api_instance.get_dashboard_widgets(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsApi->get_dashboard_widgets: %s\n" % e)
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
dashboard-id | DashboardIdSchema | | 

# DashboardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dashboard_widgets.ApiResponseFor200) | Successfully returned the widgets for the dashboard
404 | [ApiResponseFor404](#get_dashboard_widgets.ApiResponseFor404) | Dashboard with id not found

#### get_dashboard_widgets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Widget**](../../models/Widget.md) |  | 


#### get_dashboard_widgets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_dashboard_widget**
<a name="post_dashboard_widget"></a>
> post_dashboard_widget(dashboard_idwidget)

Adds widget to dashboard

Create a new widget and add this to a dashboard

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import widgets_api
from eliona/api_client.model.widget import Widget
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
    api_instance = widgets_api.WidgetsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dashboard-id': 4711,
    }
    query_params = {
    }
    body = Widget(
        id=4711,
        widget_type_name="Weather",
        details=dict(),
        asset_id=4711,
        sequence=1,
        data=[
            WidgetData(
                id=4711,
                element_sequence=1,
                asset_id=4711,
                data=dict(),
            )
        ],
    )
    try:
        # Adds widget to dashboard
        api_response = api_instance.post_dashboard_widget(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsApi->post_dashboard_widget: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dashboard-id': 4711,
    }
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    body = Widget(
        id=4711,
        widget_type_name="Weather",
        details=dict(),
        asset_id=4711,
        sequence=1,
        data=[
            WidgetData(
                id=4711,
                element_sequence=1,
                asset_id=4711,
                data=dict(),
            )
        ],
    )
    try:
        # Adds widget to dashboard
        api_response = api_instance.post_dashboard_widget(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsApi->post_dashboard_widget: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Widget**](../../models/Widget.md) |  | 


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
dashboard-id | DashboardIdSchema | | 

# DashboardIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_dashboard_widget.ApiResponseFor201) | Successfully added widget
404 | [ApiResponseFor404](#post_dashboard_widget.ApiResponseFor404) | Dashboard with id not found

#### post_dashboard_widget.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### post_dashboard_widget.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


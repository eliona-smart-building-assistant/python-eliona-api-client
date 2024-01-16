# eliona.api_client.WidgetsApi

All URIs are relative to *https://name.eliona.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_widgets**](WidgetsApi.md#get_dashboard_widgets) | **GET** /dashboards/{dashboard-id}/widgets | Information about widgets on dashboard
[**post_dashboard_widget**](WidgetsApi.md#post_dashboard_widget) | **POST** /dashboards/{dashboard-id}/widgets | Adds widget to dashboard


# **get_dashboard_widgets**
> Widget get_dashboard_widgets(dashboard_id)

Information about widgets on dashboard

Gets information about widgets on a dashboard.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import widgets_api
from eliona.api_client.model.widget import Widget
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    dashboard_id = 4711 # int | The id of the dashboard
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Information about widgets on dashboard
        api_response = api_instance.get_dashboard_widgets(dashboard_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsApi->get_dashboard_widgets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about widgets on dashboard
        api_response = api_instance.get_dashboard_widgets(dashboard_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsApi->get_dashboard_widgets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| The id of the dashboard |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**Widget**](Widget.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the widgets for the dashboard |  -  |
**404** | Dashboard with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dashboard_widget**
> post_dashboard_widget(dashboard_id, widget)

Adds widget to dashboard

Create a new widget and add this to a dashboard

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import widgets_api
from eliona.api_client.model.widget import Widget
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    dashboard_id = 4711 # int | The id of the dashboard
    widget = Widget(
        widget_type_name="Weather",
        details={},
        asset_id=4711,
        sequence=1,
        data=[
            WidgetData(
                element_sequence=1,
                asset_id=4711,
                data={},
            ),
        ],
    ) # Widget | 
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds widget to dashboard
        api_instance.post_dashboard_widget(dashboard_id, widget)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsApi->post_dashboard_widget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds widget to dashboard
        api_instance.post_dashboard_widget(dashboard_id, widget, expansions=expansions)
    except eliona.api_client.ApiException as e:
        print("Exception when calling WidgetsApi->post_dashboard_widget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| The id of the dashboard |
 **widget** | [**Widget**](Widget.md)|  |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

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
**201** | Successfully added widget |  -  |
**404** | Dashboard with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


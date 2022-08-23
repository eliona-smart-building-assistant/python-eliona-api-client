# eliona.api_client.DashboardsApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_dashboard**](DashboardsApi.md#post_dashboard) | **POST** /dashboards | Creates a new dashboard
[**post_dashboard_widget**](DashboardsApi.md#post_dashboard_widget) | **POST** /dashboards/{dashboard-id}/widgets | Adds widget to dashboard
[**put_widget_type**](DashboardsApi.md#put_widget_type) | **PUT** /widget-types | Create or update a widget type


# **post_dashboard**
> Dashboard post_dashboard(dashboard)

Creates a new dashboard

Create a new dashboard for frontend

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import dashboards_api
from eliona.api_client.model.dashboard import Dashboard
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

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard = Dashboard(
        name="Weather info",
        project_id="99",
        user_id="42",
        sequence=1,
    ) # Dashboard | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new dashboard
        api_response = api_instance.post_dashboard(dashboard)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DashboardsApi->post_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard** | [**Dashboard**](Dashboard.md)|  |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added a new Dashboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dashboard_widget**
> post_dashboard_widget(dashboard_id, widget)

Adds widget to dashboard

Create a new widget an ad this to a dashboard

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import dashboards_api
from eliona.api_client.model.widget import Widget
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

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = 4711 # int | The id of the dashboard
    widget = Widget(
        widget_type_name="Weather",
        width="normal",
        timespan=7,
        details={},
        asset_id=4711,
        data=[
            WidgetData(
                element_sequence=1,
                key="key_example",
                asset_id=4711,
                subtype=HeapSubtype("input"),
                attribute="temperature",
                description="Temperature",
            ),
        ],
    ) # Widget | 

    # example passing only required values which don't have defaults set
    try:
        # Adds widget to dashboard
        api_instance.post_dashboard_widget(dashboard_id, widget)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DashboardsApi->post_dashboard_widget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| The id of the dashboard |
 **widget** | [**Widget**](Widget.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added widget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_widget_type**
> put_widget_type(widget_type)

Create or update a widget type

Create a widget type if the a type with the name not exists or update a widget type if the name already exists

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import dashboards_api
from eliona.api_client.model.widget_type import WidgetType
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

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboards_api.DashboardsApi(api_client)
    widget_type = WidgetType(
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
                category="weather",
                description="Weather",
                config={},
            ),
        ],
    ) # WidgetType | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update a widget type
        api_instance.put_widget_type(widget_type)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DashboardsApi->put_widget_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type** | [**WidgetType**](WidgetType.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added widget type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


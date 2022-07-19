# io.eliona.api_client.DashboardApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_dashboard**](DashboardApi.md#post_dashboard) | **POST** /dashboard | Creates a new dashboard
[**post_widget_type**](DashboardApi.md#post_widget_type) | **POST** /widget-type | Adds a new widget type
[**put_dashboard_widget**](DashboardApi.md#put_dashboard_widget) | **PUT** /dashboard/{dashboard-id}/widget | Adds widget to dashboard


# **post_dashboard**
> Dashboard post_dashboard(dashboard)

Creates a new dashboard

Create a new dashboard for frontend

### Example


```python
import time
import io.eliona.api_client
from io.eliona.api_client.api import dashboard_api
from io.eliona.api_client.model.dashboard import Dashboard
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with io.eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dashboard_api.DashboardApi(api_client)
    dashboard = Dashboard(
        id=4711,
        name="Weather info",
        project_id="99",
        user_id="42",
    ) # Dashboard | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new dashboard
        api_response = api_instance.post_dashboard(dashboard)
        pprint(api_response)
    except io.eliona.api_client.ApiException as e:
        print("Exception when calling DashboardApi->post_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard** | [**Dashboard**](Dashboard.md)|  |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added a new Dashboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_widget_type**
> post_widget_type(widget_type)

Adds a new widget type

Create a new widget type

### Example


```python
import time
import io.eliona.api_client
from io.eliona.api_client.api import dashboard_api
from io.eliona.api_client.model.widget_type import WidgetType
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with io.eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dashboard_api.DashboardApi(api_client)
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
        # Adds a new widget type
        api_instance.post_widget_type(widget_type)
    except io.eliona.api_client.ApiException as e:
        print("Exception when calling DashboardApi->post_widget_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type** | [**WidgetType**](WidgetType.md)|  |

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
**200** | Successfully added widget type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_dashboard_widget**
> put_dashboard_widget(dashboard_id, widget)

Adds widget to dashboard

Create a new widget an ad this to a dashboard

### Example


```python
import time
import io.eliona.api_client
from io.eliona.api_client.api import dashboard_api
from io.eliona.api_client.model.widget import Widget
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with io.eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dashboard_api.DashboardApi(api_client)
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
        api_instance.put_dashboard_widget(dashboard_id, widget)
    except io.eliona.api_client.ApiException as e:
        print("Exception when calling DashboardApi->put_dashboard_widget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| The id of the dashboard |
 **widget** | [**Widget**](Widget.md)|  |

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
**200** | Successfully added widget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


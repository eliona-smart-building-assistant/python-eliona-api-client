# eliona.api_client.DashboardsApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_by_id**](DashboardsApi.md#get_dashboard_by_id) | **GET** /dashboards/{dashboard-id} | Information about a dashboard
[**get_dashboards**](DashboardsApi.md#get_dashboards) | **GET** /dashboards | Information about dashboards
[**post_dashboard**](DashboardsApi.md#post_dashboard) | **POST** /dashboards | Creates a new dashboard


# **get_dashboard_by_id**
> Dashboard get_dashboard_by_id(dashboard_id)

Information about a dashboard

Gets information about a dashboard.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import dashboards_api
from eliona.api_client.model.dashboard import Dashboard
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
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
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard_id = 4711 # int | The id of the dashboard
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Information about a dashboard
        api_response = api_instance.get_dashboard_by_id(dashboard_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DashboardsApi->get_dashboard_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about a dashboard
        api_response = api_instance.get_dashboard_by_id(dashboard_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DashboardsApi->get_dashboard_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| The id of the dashboard |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the the dashboard |  -  |
**404** | Dashboard with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboards**
> [Dashboard] get_dashboards()

Information about dashboards

Gets a list of dashboards

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import dashboards_api
from eliona.api_client.model.dashboard import Dashboard
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
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
    api_instance = dashboards_api.DashboardsApi(api_client)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about dashboards
        api_response = api_instance.get_dashboards(expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DashboardsApi->get_dashboards: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[Dashboard]**](Dashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of dashboards |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dashboard**
> Dashboard post_dashboard(dashboard)

Creates a new dashboard

Create a new dashboard for frontend

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import dashboards_api
from eliona.api_client.model.dashboard import Dashboard
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
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
    api_instance = dashboards_api.DashboardsApi(api_client)
    dashboard = Dashboard(
        name="Weather info",
        project_id="99",
        user_id="42",
        sequence=1,
        widgets=[
            Widget(
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
            ),
        ],
        public=False,
    ) # Dashboard | 
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a new dashboard
        api_response = api_instance.post_dashboard(dashboard)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DashboardsApi->post_dashboard: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new dashboard
        api_response = api_instance.post_dashboard(dashboard, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DashboardsApi->post_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard** | [**Dashboard**](Dashboard.md)|  |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully added a new Dashboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


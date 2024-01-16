# eliona.api_client.AlarmsApi

All URIs are relative to *https://name.eliona.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alarm_by_id**](AlarmsApi.md#get_alarm_by_id) | **GET** /alarms/{alarm-rule-id} | Information about alarm
[**get_alarm_history_by_id**](AlarmsApi.md#get_alarm_history_by_id) | **GET** /alarms-history/{alarm-rule-id} | Information about alarm history
[**get_alarms**](AlarmsApi.md#get_alarms) | **GET** /alarms | Information about alarms
[**get_alarms_history**](AlarmsApi.md#get_alarms_history) | **GET** /alarms-history | Information about alarms history
[**get_highest_alarms**](AlarmsApi.md#get_highest_alarms) | **GET** /alarms-highest | Information about most prioritized alarms
[**listen_alarm**](AlarmsApi.md#listen_alarm) | **GET** /alarm-listener | WebSocket connection for alarm changes
[**patch_alarm_by_id**](AlarmsApi.md#patch_alarm_by_id) | **PATCH** /alarms/{alarm-rule-id} | Update alarm


# **get_alarm_by_id**
> Alarm get_alarm_by_id(alarm_rule_id)

Information about alarm

Gets information about alarm.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarms_api
from eliona.api_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Information about alarm
        api_response = api_instance.get_alarm_by_id(alarm_rule_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_alarm_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about alarm
        api_response = api_instance.get_alarm_by_id(alarm_rule_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_alarm_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**Alarm**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an alarm |  -  |
**404** | Alarm with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_history_by_id**
> [Alarm] get_alarm_history_by_id(alarm_rule_id)

Information about alarm history

Gets information about alarm over the entire time. This includes current alarm and history.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarms_api
from eliona.api_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Information about alarm history
        api_response = api_instance.get_alarm_history_by_id(alarm_rule_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_alarm_history_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about alarm history
        api_response = api_instance.get_alarm_history_by_id(alarm_rule_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_alarm_history_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[Alarm]**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarms**
> [Alarm] get_alarms()

Information about alarms

Gets information about alarms

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarms_api
from eliona.api_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    project_id = "projectId_example" # str, none_type | Filter for a specific project (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about alarms
        api_response = api_instance.get_alarms(project_id=project_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_alarms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str, none_type**| Filter for a specific project | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[Alarm]**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarms_history**
> [Alarm] get_alarms_history()

Information about alarms history

Gets information about alarms over the entire time. This includes current alarms and alarms, which are already processed.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarms_api
from eliona.api_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    project_id = "projectId_example" # str, none_type | Filter for a specific project (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about alarms history
        api_response = api_instance.get_alarms_history(project_id=project_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_alarms_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str, none_type**| Filter for a specific project | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[Alarm]**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_highest_alarms**
> [Alarm] get_highest_alarms()

Information about most prioritized alarms

Gets information about an alarms with the highest priority for each asset.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarms_api
from eliona.api_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    project_id = "projectId_example" # str, none_type | Filter for a specific project (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about most prioritized alarms
        api_response = api_instance.get_highest_alarms(project_id=project_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_highest_alarms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str, none_type**| Filter for a specific project | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[Alarm]**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of most prioritized alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_alarm**
> Alarm listen_alarm()

WebSocket connection for alarm changes

Open a WebSocket connection to get informed when new alarm data is written or anything changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarms_api
from eliona.api_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # WebSocket connection for alarm changes
        api_response = api_instance.listen_alarm()
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->listen_alarm: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Alarm**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully opened a connection to alarm WebSocket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_alarm_by_id**
> patch_alarm_by_id(alarm_rule_id, acknowledged)

Update alarm

Update properties of alarm for given id.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarms_api
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
    api_instance = alarms_api.AlarmsApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    acknowledged = True # bool | Marks the alarm as acknowledged or not acknowledged by setting the acknowledge timestamp to now or to null.
    acknowledge_text = "acknowledgeText_example" # str | Sets the text for acknowledgement if acknowledged is set to true (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update alarm
        api_instance.patch_alarm_by_id(alarm_rule_id, acknowledged)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->patch_alarm_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update alarm
        api_instance.patch_alarm_by_id(alarm_rule_id, acknowledged, acknowledge_text=acknowledge_text)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmsApi->patch_alarm_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule |
 **acknowledged** | **bool**| Marks the alarm as acknowledged or not acknowledged by setting the acknowledge timestamp to now or to null. |
 **acknowledge_text** | **str**| Sets the text for acknowledgement if acknowledged is set to true | [optional]

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
**200** | Successfully updated the alarm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


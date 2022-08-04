# eliona.api_client.AlarmRulesApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alarm_rule_by_id**](AlarmRulesApi.md#get_alarm_rule_by_id) | **GET** /alarm-rules/{alarm-rule-id} | Information about an alarm rule
[**get_alarm_rules**](AlarmRulesApi.md#get_alarm_rules) | **GET** /alarm-rules | Information about alarm rules
[**put_alarm_rule**](AlarmRulesApi.md#put_alarm_rule) | **PUT** /alarm-rules | Create or update an alarm rule


# **get_alarm_rule_by_id**
> AlarmRule get_alarm_rule_by_id(alarm_rule_id)

Information about an alarm rule

Gets information about an alarm rule.

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from eliona.api_client.model.alarm_rule import AlarmRule
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Information about an alarm rule
        api_response = api_instance.get_alarm_rule_by_id(alarm_rule_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rule_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about an alarm rule
        api_response = api_instance.get_alarm_rule_by_id(alarm_rule_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rule_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule |
 **expansions** | **[str], none_type**| List of referenced data to load. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an alarm rule |  -  |
**404** | Alarm rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_rules**
> [AlarmRule] get_alarm_rules()

Information about alarm rules

Gets information about alarm rules.

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from eliona.api_client.model.alarm_rule import AlarmRule
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about alarm rules
        api_response = api_instance.get_alarm_rules(expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expansions** | **[str], none_type**| List of referenced data to load. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[AlarmRule]**](AlarmRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alarm_rule**
> put_alarm_rule(alarm_rule)

Create or update an alarm rule

Create a new alarm rule or update an alarm rule if already exists

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from eliona.api_client.model.alarm_rule import AlarmRule
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    alarm_rule = AlarmRule(
        asset_id=4711,
        subtype=HeapSubtype("input"),
        attribute="temperature",
        enable=True,
        priority=AlarmPriority(2),
        requires_acknowledge=False,
        equal=38.7,
        low=38.7,
        high=38.7,
        message={},
        tags=[
            "tags_example",
        ],
        subject="subject_example",
        urldoc="urldoc_example",
        notify_on="notify_on_example",
        dont_mask=False,
        asset_info=Asset(
            project_id="99",
            global_asset_identifier="zurich_swiss",
            name="Station Zurich",
            asset_type="asset_type_example",
            latitude=47.3667,
            longitude=8.55,
            description="Weather station Zurich, Swiss",
            parent_functional_asset_id=4712,
            parent_locational_asset_id=4712,
            tags=["weather","location"],
        ),
    ) # AlarmRule | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an alarm rule
        api_instance.put_alarm_rule(alarm_rule)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->put_alarm_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule** | [**AlarmRule**](AlarmRule.md)|  |

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
**200** | Successfully created a new or updated an existing alarm rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="__pageTop"></a>
# eliona.api_client.apis.tags.alarm_rules_api.AlarmRulesApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alarm_rule_by_id**](#get_alarm_rule_by_id) | **get** /alarm-rules/{alarm-rule-id} | Information about an alarm rule
[**get_alarm_rules**](#get_alarm_rules) | **get** /alarm-rules | Information about alarm rules
[**post_alarm_rule**](#post_alarm_rule) | **post** /alarm-rules | Create an alarm rule
[**put_alarm_rule**](#put_alarm_rule) | **put** /alarm-rules | Create or update an alarm rule
[**put_alarm_rule_by_id**](#put_alarm_rule_by_id) | **put** /alarm-rules/{alarm-rule-id} | Update an alarm rule

# **get_alarm_rule_by_id**
<a name="get_alarm_rule_by_id"></a>
> AlarmRule get_alarm_rule_by_id(alarm_rule_id)

Information about an alarm rule

Gets information about an alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import alarm_rules_api
from eliona/api_client.model.alarm_rule import AlarmRule
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
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'alarm-rule-id': 4711,
    }
    query_params = {
    }
    try:
        # Information about an alarm rule
        api_response = api_instance.get_alarm_rule_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rule_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'alarm-rule-id': 4711,
    }
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    try:
        # Information about an alarm rule
        api_response = api_instance.get_alarm_rule_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rule_by_id: %s\n" % e)
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
alarm-rule-id | AlarmRuleIdSchema | | 

# AlarmRuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_alarm_rule_by_id.ApiResponseFor200) | Successfully returned an alarm rule
404 | [ApiResponseFor404](#get_alarm_rule_by_id.ApiResponseFor404) | Alarm rule with id not found

#### get_alarm_rule_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AlarmRule**](../../models/AlarmRule.md) |  | 


#### get_alarm_rule_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_alarm_rules**
<a name="get_alarm_rules"></a>
> [AlarmRule] get_alarm_rules()

Information about alarm rules

Gets information about alarm rules.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import alarm_rules_api
from eliona/api_client.model.alarm_rule import AlarmRule
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
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)

    # example passing only optional values
    query_params = {
        'expansions': [
        "expansions_example"
    ],
    }
    try:
        # Information about alarm rules
        api_response = api_instance.get_alarm_rules(
            query_params=query_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rules: %s\n" % e)
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
200 | [ApiResponseFor200](#get_alarm_rules.ApiResponseFor200) | Successfully returned a list of alarms

#### get_alarm_rules.ApiResponseFor200
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
[**AlarmRule**]({{complexTypePrefix}}AlarmRule.md) | [**AlarmRule**]({{complexTypePrefix}}AlarmRule.md) | [**AlarmRule**]({{complexTypePrefix}}AlarmRule.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_alarm_rule**
<a name="post_alarm_rule"></a>
> AlarmRule post_alarm_rule(alarm_rule)

Create an alarm rule

Create a new alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import alarm_rules_api
from eliona/api_client.model.alarm_rule import AlarmRule
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
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)

    # example passing only required values which don't have defaults set
    body = AlarmRule(
        id=123,
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        enable=True,
        priority=AlarmPriority(2),
        requires_acknowledge=False,
        equal=38.7,
        low=38.7,
        high=38.7,
        message=dict(),
        tags=[
            "tags_example"
        ],
        subject="subject_example",
        urldoc="urldoc_example",
        notify_on="R",
        dont_mask=False,
        asset_info=Asset(
            id=4711,
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
            children_info=[
                Asset()
            ],
        ),
    )
    try:
        # Create an alarm rule
        api_response = api_instance.post_alarm_rule(
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->post_alarm_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AlarmRule**](../../models/AlarmRule.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_alarm_rule.ApiResponseFor201) | Successfully created a new alarm rule

#### post_alarm_rule.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AlarmRule**](../../models/AlarmRule.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_alarm_rule**
<a name="put_alarm_rule"></a>
> AlarmRule put_alarm_rule(alarm_rule)

Create or update an alarm rule

Deprecated - Use POST /alarm-rules to create and PUT /alarm-rules/{alarm-rule-id} to update

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import alarm_rules_api
from eliona/api_client.model.alarm_rule import AlarmRule
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
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)

    # example passing only required values which don't have defaults set
    body = AlarmRule(
        id=123,
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        enable=True,
        priority=AlarmPriority(2),
        requires_acknowledge=False,
        equal=38.7,
        low=38.7,
        high=38.7,
        message=dict(),
        tags=[
            "tags_example"
        ],
        subject="subject_example",
        urldoc="urldoc_example",
        notify_on="R",
        dont_mask=False,
        asset_info=Asset(
            id=4711,
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
            children_info=[
                Asset()
            ],
        ),
    )
    try:
        # Create or update an alarm rule
        api_response = api_instance.put_alarm_rule(
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->put_alarm_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AlarmRule**](../../models/AlarmRule.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_alarm_rule.ApiResponseFor200) | Successfully created a new or updated an existing alarm rule

#### put_alarm_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AlarmRule**](../../models/AlarmRule.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_alarm_rule_by_id**
<a name="put_alarm_rule_by_id"></a>
> AlarmRule put_alarm_rule_by_id(alarm_rule_idalarm_rule)

Update an alarm rule

Update an alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import alarm_rules_api
from eliona/api_client.model.alarm_rule import AlarmRule
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
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'alarm-rule-id': 4711,
    }
    body = AlarmRule(
        id=123,
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        enable=True,
        priority=AlarmPriority(2),
        requires_acknowledge=False,
        equal=38.7,
        low=38.7,
        high=38.7,
        message=dict(),
        tags=[
            "tags_example"
        ],
        subject="subject_example",
        urldoc="urldoc_example",
        notify_on="R",
        dont_mask=False,
        asset_info=Asset(
            id=4711,
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
            children_info=[
                Asset()
            ],
        ),
    )
    try:
        # Update an alarm rule
        api_response = api_instance.put_alarm_rule_by_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->put_alarm_rule_by_id: %s\n" % e)
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
[**AlarmRule**](../../models/AlarmRule.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
alarm-rule-id | AlarmRuleIdSchema | | 

# AlarmRuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_alarm_rule_by_id.ApiResponseFor200) | Successfully updated an existing alarm rule
404 | [ApiResponseFor404](#put_alarm_rule_by_id.ApiResponseFor404) | Alarm rule with id not found

#### put_alarm_rule_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AlarmRule**](../../models/AlarmRule.md) |  | 


#### put_alarm_rule_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


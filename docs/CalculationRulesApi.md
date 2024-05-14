# eliona.api_client.CalculationRulesApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_calculation_rule_by_id**](CalculationRulesApi.md#delete_calculation_rule_by_id) | **DELETE** /calculation-rules/{calculation-rule-id} | Delete a calculation rule
[**get_calculation_rule_by_id**](CalculationRulesApi.md#get_calculation_rule_by_id) | **GET** /calculation-rules/{calculation-rule-id} | Information about a calculation rules rule
[**get_calculation_rules**](CalculationRulesApi.md#get_calculation_rules) | **GET** /calculation-rules | Information about calculation rules
[**put_calculation_rule**](CalculationRulesApi.md#put_calculation_rule) | **PUT** /calculation-rules | Creates or updates a calculation rule
[**put_calculation_rule_by_id**](CalculationRulesApi.md#put_calculation_rule_by_id) | **PUT** /calculation-rules/{calculation-rule-id} | Update a calculation rule


# **delete_calculation_rule_by_id**
> delete_calculation_rule_by_id(calculation_rule_id)

Delete a calculation rule

Deletes a calculation rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import calculation_rules_api
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
    api_instance = calculation_rules_api.CalculationRulesApi(api_client)
    calculation_rule_id = 4711 # int | The id of the calculation rule

    # example passing only required values which don't have defaults set
    try:
        # Delete a calculation rule
        api_instance.delete_calculation_rule_by_id(calculation_rule_id)
    except eliona.api_client.ApiException as e:
        print("Exception when calling CalculationRulesApi->delete_calculation_rule_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule_id** | **int**| The id of the calculation rule |

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
**204** | Successfully deleted the calculation rule |  -  |
**404** | Calculation rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculation_rule_by_id**
> CalculationRule get_calculation_rule_by_id(calculation_rule_id)

Information about a calculation rules rule

Gets information about a calculation rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import calculation_rules_api
from eliona.api_client.model.calculation_rule import CalculationRule
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
    api_instance = calculation_rules_api.CalculationRulesApi(api_client)
    calculation_rule_id = 4711 # int | The id of the calculation rule

    # example passing only required values which don't have defaults set
    try:
        # Information about a calculation rules rule
        api_response = api_instance.get_calculation_rule_by_id(calculation_rule_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling CalculationRulesApi->get_calculation_rule_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule_id** | **int**| The id of the calculation rule |

### Return type

[**CalculationRule**](CalculationRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned ancalculation rule |  -  |
**404** | Calculation rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculation_rules**
> [CalculationRule] get_calculation_rules()

Information about calculation rules

Gets information about calculation rules.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import calculation_rules_api
from eliona.api_client.model.calculation_rule import CalculationRule
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
    api_instance = calculation_rules_api.CalculationRulesApi(api_client)
    calculation_rule_ids = [
        1,
    ] # [int], none_type | List of calculation rule ids for filtering (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about calculation rules
        api_response = api_instance.get_calculation_rules(calculation_rule_ids=calculation_rule_ids)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling CalculationRulesApi->get_calculation_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule_ids** | **[int], none_type**| List of calculation rule ids for filtering | [optional]

### Return type

[**[CalculationRule]**](CalculationRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of calculation rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_calculation_rule**
> CalculationRule put_calculation_rule(calculation_rule)

Creates or updates a calculation rule

Creates a new or updates an existing calculation rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import calculation_rules_api
from eliona.api_client.model.calculation_rule import CalculationRule
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
    api_instance = calculation_rules_api.CalculationRulesApi(api_client)
    calculation_rule = CalculationRule(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        virtual=True,
        formula="{seconds} * 60",
        unit="°C",
        filter={},
    ) # CalculationRule | 

    # example passing only required values which don't have defaults set
    try:
        # Creates or updates a calculation rule
        api_response = api_instance.put_calculation_rule(calculation_rule)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling CalculationRulesApi->put_calculation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule** | [**CalculationRule**](CalculationRule.md)|  |

### Return type

[**CalculationRule**](CalculationRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created or updated a calculation rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_calculation_rule_by_id**
> CalculationRule put_calculation_rule_by_id(calculation_rule_id, calculation_rule)

Update a calculation rule

Update a calculation rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import calculation_rules_api
from eliona.api_client.model.calculation_rule import CalculationRule
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
    api_instance = calculation_rules_api.CalculationRulesApi(api_client)
    calculation_rule_id = 4711 # int | The id of the calculation rule
    calculation_rule = CalculationRule(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        virtual=True,
        formula="{seconds} * 60",
        unit="°C",
        filter={},
    ) # CalculationRule | 

    # example passing only required values which don't have defaults set
    try:
        # Update a calculation rule
        api_response = api_instance.put_calculation_rule_by_id(calculation_rule_id, calculation_rule)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling CalculationRulesApi->put_calculation_rule_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule_id** | **int**| The id of the calculation rule |
 **calculation_rule** | [**CalculationRule**](CalculationRule.md)|  |

### Return type

[**CalculationRule**](CalculationRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing calculation rule |  -  |
**404** | Calculation rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


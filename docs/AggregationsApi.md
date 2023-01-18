# eliona.api_client.AggregationsApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_aggregation_by_id**](AggregationsApi.md#delete_aggregation_by_id) | **DELETE** /aggregations/{aggregation-id} | Delete an aggregation
[**get_aggregation_by_id**](AggregationsApi.md#get_aggregation_by_id) | **GET** /aggregations/{aggregation-id} | Information about an aggregation
[**get_aggregations**](AggregationsApi.md#get_aggregations) | **GET** /aggregations | Information about aggregations
[**post_aggregation**](AggregationsApi.md#post_aggregation) | **POST** /aggregations | Creates an aggregation
[**put_aggregation**](AggregationsApi.md#put_aggregation) | **PUT** /aggregations | Creates or updates an aggregation
[**put_aggregation_by_id**](AggregationsApi.md#put_aggregation_by_id) | **PUT** /aggregations/{aggregation-id} | Updates an aggregation


# **delete_aggregation_by_id**
> delete_aggregation_by_id(aggregation_id)

Delete an aggregation

Deletes an aggregation by the given id.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import aggregations_api
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
    api_instance = aggregations_api.AggregationsApi(api_client)
    aggregation_id = 4711 # int | The id of the aggregation

    # example passing only required values which don't have defaults set
    try:
        # Delete an aggregation
        api_instance.delete_aggregation_by_id(aggregation_id)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AggregationsApi->delete_aggregation_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation_id** | **int**| The id of the aggregation |

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
**204** | Successfully deleted the aggregation by id. |  -  |
**404** | Aggregation with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_by_id**
> Aggregation get_aggregation_by_id(aggregation_id)

Information about an aggregation

Gets information about an aggregation by the given id.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import aggregations_api
from eliona.api_client.model.aggregation import Aggregation
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
    api_instance = aggregations_api.AggregationsApi(api_client)
    aggregation_id = 4711 # int | The id of the aggregation

    # example passing only required values which don't have defaults set
    try:
        # Information about an aggregation
        api_response = api_instance.get_aggregation_by_id(aggregation_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AggregationsApi->get_aggregation_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation_id** | **int**| The id of the aggregation |

### Return type

[**Aggregation**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an aggregation by id. |  -  |
**404** | Aggregation with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregations**
> [Aggregation] get_aggregations()

Information about aggregations

Gets a list of aggregations

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import aggregations_api
from eliona.api_client.model.aggregation import Aggregation
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
    api_instance = aggregations_api.AggregationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Information about aggregations
        api_response = api_instance.get_aggregations()
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AggregationsApi->get_aggregations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Aggregation]**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of aggregations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_aggregation**
> Aggregation post_aggregation(aggregation)

Creates an aggregation

Creates a new aggregation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import aggregations_api
from eliona.api_client.model.aggregation import Aggregation
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
    api_instance = aggregations_api.AggregationsApi(api_client)
    aggregation = Aggregation(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        mode="avg",
        raster="DAY",
    ) # Aggregation | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an aggregation
        api_response = api_instance.post_aggregation(aggregation)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AggregationsApi->post_aggregation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation** | [**Aggregation**](Aggregation.md)|  |

### Return type

[**Aggregation**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created an aggregation |  -  |
**409** | Combination of asset id, subtype, attribute and raster already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_aggregation**
> Aggregation put_aggregation(aggregation)

Creates or updates an aggregation

Creates an aggregation or updates if already exists. Uses the unique combination of asset id, subtype, attribute and raster for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import aggregations_api
from eliona.api_client.model.aggregation import Aggregation
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
    api_instance = aggregations_api.AggregationsApi(api_client)
    aggregation = Aggregation(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        mode="avg",
        raster="DAY",
    ) # Aggregation | 

    # example passing only required values which don't have defaults set
    try:
        # Creates or updates an aggregation
        api_response = api_instance.put_aggregation(aggregation)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AggregationsApi->put_aggregation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation** | [**Aggregation**](Aggregation.md)|  |

### Return type

[**Aggregation**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created or updated an aggregation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_aggregation_by_id**
> Aggregation put_aggregation_by_id(aggregation_id, aggregation)

Updates an aggregation

Updates an aggregation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import aggregations_api
from eliona.api_client.model.aggregation import Aggregation
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
    api_instance = aggregations_api.AggregationsApi(api_client)
    aggregation_id = 4711 # int | The id of the aggregation
    aggregation = Aggregation(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        mode="avg",
        raster="DAY",
    ) # Aggregation | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an aggregation
        api_response = api_instance.put_aggregation_by_id(aggregation_id, aggregation)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AggregationsApi->put_aggregation_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation_id** | **int**| The id of the aggregation |
 **aggregation** | [**Aggregation**](Aggregation.md)|  |

### Return type

[**Aggregation**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an aggregation |  -  |
**404** | Aggregation with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


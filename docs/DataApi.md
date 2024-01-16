# eliona.api_client.DataApi

All URIs are relative to *https://name.eliona.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data**](DataApi.md#get_data) | **GET** /data | Gets all data
[**get_data_aggregated**](DataApi.md#get_data_aggregated) | **GET** /data-aggregated | Get aggregated data
[**get_data_trends**](DataApi.md#get_data_trends) | **GET** /data-trends | Get trend of historical data
[**listen_data**](DataApi.md#listen_data) | **GET** /data-listener | WebSocket connection for asset data changes
[**put_bulk_data**](DataApi.md#put_bulk_data) | **PUT** /data-bulk | Create or update multiple asset data
[**put_data**](DataApi.md#put_data) | **PUT** /data | Create or update asset data


# **get_data**
> [Data] get_data()

Gets all data

Gets information about data for assets.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import data_api
from eliona.api_client.model.data import Data
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
    api_instance = data_api.DataApi(api_client)
    asset_id = 4711 # int | Filter for a specific asset id (optional)
    parent_asset_id = 4711 # int | Filter for a specific parent asset id (optional)
    data_subtype = "input" # str | Filter for a specific type of asset data (optional)
    asset_type_name = "weather_location" # str | Filter the name of the asset type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets all data
        api_response = api_instance.get_data(asset_id=asset_id, parent_asset_id=parent_asset_id, data_subtype=data_subtype, asset_type_name=asset_type_name)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->get_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| Filter for a specific asset id | [optional]
 **parent_asset_id** | **int**| Filter for a specific parent asset id | [optional]
 **data_subtype** | **str**| Filter for a specific type of asset data | [optional]
 **asset_type_name** | **str**| Filter the name of the asset type | [optional]

### Return type

[**[Data]**](Data.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned data for assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_aggregated**
> [DataAggregated] get_data_aggregated()

Get aggregated data

Gets aggregated data sets which combines a set of data points for a defined periodical raster

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import data_api
from eliona.api_client.model.data_aggregated import DataAggregated
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
    api_instance = data_api.DataApi(api_client)
    from_date = "2020-01-01T09:00:00.000Z" # str | Filter by lower date time (RFC3339) limit inclusive (optional)
    to_date = "2021-12-31T23:00:00.000Z" # str | Filter by upper date time (RFC3339) limit exclusive (optional)
    asset_id = 4711 # int | Filter for a specific asset id (optional)
    data_subtype = "input" # str | Filter for a specific type of asset data (optional)
    asset_type_name = "weather_location" # str | Filter the name of the asset type (optional)
    aggregation_id = 0815 # int | Filter for a specific aggregation id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get aggregated data
        api_response = api_instance.get_data_aggregated(from_date=from_date, to_date=to_date, asset_id=asset_id, data_subtype=data_subtype, asset_type_name=asset_type_name, aggregation_id=aggregation_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->get_data_aggregated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **str**| Filter by lower date time (RFC3339) limit inclusive | [optional]
 **to_date** | **str**| Filter by upper date time (RFC3339) limit exclusive | [optional]
 **asset_id** | **int**| Filter for a specific asset id | [optional]
 **data_subtype** | **str**| Filter for a specific type of asset data | [optional]
 **asset_type_name** | **str**| Filter the name of the asset type | [optional]
 **aggregation_id** | **int**| Filter for a specific aggregation id | [optional]

### Return type

[**[DataAggregated]**](DataAggregated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned aggregated data sets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_trends**
> [Data] get_data_trends()

Get trend of historical data

Gets trend information about historical data for assets.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import data_api
from eliona.api_client.model.data import Data
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
    api_instance = data_api.DataApi(api_client)
    from_date = "2020-01-01T09:00:00.000Z" # str | Filter by lower date time (RFC3339) limit inclusive (optional)
    to_date = "2021-12-31T23:00:00.000Z" # str | Filter by upper date time (RFC3339) limit exclusive (optional)
    asset_id = 4711 # int | Filter for a specific asset id (optional)
    data_subtype = "input" # str | Filter for a specific type of asset data (optional)
    asset_type_name = "weather_location" # str | Filter the name of the asset type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get trend of historical data
        api_response = api_instance.get_data_trends(from_date=from_date, to_date=to_date, asset_id=asset_id, data_subtype=data_subtype, asset_type_name=asset_type_name)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->get_data_trends: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **str**| Filter by lower date time (RFC3339) limit inclusive | [optional]
 **to_date** | **str**| Filter by upper date time (RFC3339) limit exclusive | [optional]
 **asset_id** | **int**| Filter for a specific asset id | [optional]
 **data_subtype** | **str**| Filter for a specific type of asset data | [optional]
 **asset_type_name** | **str**| Filter the name of the asset type | [optional]

### Return type

[**[Data]**](Data.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned historical data for assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_data**
> Data listen_data()

WebSocket connection for asset data changes

Open a WebSocket connection to get informed when new asset data is written or anything changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import data_api
from eliona.api_client.model.data import Data
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
    api_instance = data_api.DataApi(api_client)
    asset_id = 4711 # int | Filter for a specific asset id (optional)
    data_subtype = "input" # str | Filter for a specific type of asset data (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # WebSocket connection for asset data changes
        api_response = api_instance.listen_data(asset_id=asset_id, data_subtype=data_subtype)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->listen_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| Filter for a specific asset id | [optional]
 **data_subtype** | **str**| Filter for a specific type of asset data | [optional]

### Return type

[**Data**](Data.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully opened a connection to asset data WebSocket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bulk_data**
> put_bulk_data(data)

Create or update multiple asset data

Create multiple asset data or update data if already exists. Uses the unique combination of asset id and subtype for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import data_api
from eliona.api_client.model.data import Data
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
    api_instance = data_api.DataApi(api_client)
    data = [
        Data(
            asset_id=4711,
            subtype=DataSubtype("input"),
            timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            data={},
            client_reference="ABC123",
        ),
    ] # [Data] | 
    direct_mode = "true" # str | Executes the operation directly without using other services. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update multiple asset data
        api_instance.put_bulk_data(data)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->put_bulk_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update multiple asset data
        api_instance.put_bulk_data(data, direct_mode=direct_mode)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->put_bulk_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**[Data]**](Data.md)|  |
 **direct_mode** | **str**| Executes the operation directly without using other services. | [optional]

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
**201** | Successfully created multiple asset data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_data**
> put_data(data)

Create or update asset data

Create new asset data or update data if already exists. Uses the unique combination of asset id and subtype for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import data_api
from eliona.api_client.model.data import Data
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
    api_instance = data_api.DataApi(api_client)
    data = Data(
        asset_id=4711,
        subtype=DataSubtype("input"),
        timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        data={},
        client_reference="ABC123",
    ) # Data | 
    direct_mode = "true" # str | Executes the operation directly without using other services. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update asset data
        api_instance.put_data(data)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->put_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update asset data
        api_instance.put_data(data, direct_mode=direct_mode)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->put_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  |
 **direct_mode** | **str**| Executes the operation directly without using other services. | [optional]

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
**201** | Successfully created a new or updated existing asset data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


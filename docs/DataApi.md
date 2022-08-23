# eliona.api_client.DataApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_data**](DataApi.md#put_data) | **PUT** /data | Create or update asset data


# **put_data**
> put_data(data)

Create or update asset data

Create new asset data or update data if already exists

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import data_api
from eliona.api_client.model.data import Data
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
    api_instance = data_api.DataApi(api_client)
    data = Data(
        asset_id=4711,
        subtype=DataSubtype("input"),
        timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        data={},
    ) # Data | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update asset data
        api_instance.put_data(data)
    except eliona.api_client.ApiException as e:
        print("Exception when calling DataApi->put_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  |

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
**200** | Successfully created a new or updated existing asset data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


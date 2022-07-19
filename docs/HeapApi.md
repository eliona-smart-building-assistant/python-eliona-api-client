# eliona.api_client.HeapApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_heap**](HeapApi.md#post_heap) | **POST** /heap | Create or update heap data


# **post_heap**
> post_heap(heap)

Create or update heap data

Create new heap data or update data if already exists

### Example


```python
import time
import eliona.api_client
from eliona.api_client.api import heap_api
from eliona.api_client.model.heap import Heap
from pprint import pprint
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = heap_api.HeapApi(api_client)
    heap = Heap(
        asset_id=4711,
        subtype=HeapSubtype("input"),
        timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        data={},
    ) # Heap | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update heap data
        api_instance.post_heap(heap)
    except eliona.api_client.ApiException as e:
        print("Exception when calling HeapApi->post_heap: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heap** | [**Heap**](Heap.md)|  |

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
**200** | Successfully created a new or updated existing heap data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


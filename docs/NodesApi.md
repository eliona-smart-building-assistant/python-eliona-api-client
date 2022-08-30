# eliona.api_client.NodesApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_by_ident**](NodesApi.md#get_node_by_ident) | **GET** /nodes/{node-ident} | Information about a node
[**get_nodes**](NodesApi.md#get_nodes) | **GET** /nodes | Information about nodes
[**put_node**](NodesApi.md#put_node) | **PUT** /nodes | Create or update a node


# **get_node_by_ident**
> Node get_node_by_ident(node_ident)

Information about a node

Gets information about a node.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import nodes_api
from eliona.api_client.model.node import Node
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
    api_instance = nodes_api.NodesApi(api_client)
    node_ident = "4711" # str | The UUID identifier of the node

    # example passing only required values which don't have defaults set
    try:
        # Information about a node
        api_response = api_instance.get_node_by_ident(node_ident)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling NodesApi->get_node_by_ident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_ident** | **str**| The UUID identifier of the node |

### Return type

[**Node**](Node.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of node |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> [Node] get_nodes()

Information about nodes

Gets information about nodes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import nodes_api
from eliona.api_client.model.node import Node
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
    api_instance = nodes_api.NodesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Information about nodes
        api_response = api_instance.get_nodes()
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling NodesApi->get_nodes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Node]**](Node.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of nodes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_node**
> Node put_node(node)

Create or update a node

Create a new node or update a node rule if already exists

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import nodes_api
from eliona.api_client.model.node import Node
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
    api_instance = nodes_api.NodesApi(api_client)
    node = Node(
        password="password_example",
        asset_id=4711,
        vendor="vendor_example",
        model="model_example",
        description="Node east plant",
        enable=False,
    ) # Node | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update a node
        api_response = api_instance.put_node(node)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling NodesApi->put_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | [**Node**](Node.md)|  |

### Return type

[**Node**](Node.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new or updated an existing node |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


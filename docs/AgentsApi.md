# eliona.api_client.AgentsApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_device_mappings_by_id**](AgentsApi.md#get_agent_device_mappings_by_id) | **GET** /agent-devices/{agent-class}/{agent-device-id}/mappings | Information about agent device mappings
[**get_agent_devices_by_id**](AgentsApi.md#get_agent_devices_by_id) | **GET** /agents/{agent-class}/{agent-id}/devices | Information about agent devices
[**get_agents**](AgentsApi.md#get_agents) | **GET** /agents | Information about agents
[**get_agents_by_class**](AgentsApi.md#get_agents_by_class) | **GET** /agents/{agent-class} | Information about agents for a specific class
[**put_agent_by_class**](AgentsApi.md#put_agent_by_class) | **PUT** /agents/{agent-class} | Create or update an agent for a specific class
[**put_agent_device_by_id**](AgentsApi.md#put_agent_device_by_id) | **PUT** /agents/{agent-class}/{agent-id}/devices | Create or update an agent device
[**put_agent_device_mapping_by_id**](AgentsApi.md#put_agent_device_mapping_by_id) | **PUT** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create or update an agent device mapping


# **get_agent_device_mappings_by_id**
> [AgentDeviceMapping] get_agent_device_mappings_by_id(agent_class, agent_device_id)

Information about agent device mappings

Gets information about mappings between agent and eliona.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import agents_api
from eliona.api_client.model.agent_device_mapping import AgentDeviceMapping
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
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device

    # example passing only required values which don't have defaults set
    try:
        # Information about agent device mappings
        api_response = api_instance.get_agent_device_mappings_by_id(agent_class, agent_device_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_device_mappings_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_device_id** | **int**| The id of the device |

### Return type

[**[AgentDeviceMapping]**](AgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_devices_by_id**
> [AgentDevice] get_agent_devices_by_id(agent_class, agent_id)

Information about agent devices

Gets information about agent devices.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import agents_api
from eliona.api_client.model.agent_device import AgentDevice
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
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_id = 4711 # int | The id of the agent

    # example passing only required values which don't have defaults set
    try:
        # Information about agent devices
        api_response = api_instance.get_agent_devices_by_id(agent_class, agent_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_devices_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_id** | **int**| The id of the agent |

### Return type

[**[AgentDevice]**](AgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of devices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> [Agent] get_agents()

Information about agents

Gets information about agents.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import agents_api
from eliona.api_client.model.agent import Agent
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
    api_instance = agents_api.AgentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Information about agents
        api_response = api_instance.get_agents()
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agents: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Agent]**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of agents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_by_class**
> [Agent] get_agents_by_class(agent_class)

Information about agents for a specific class

Gets information about agents.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import agents_api
from eliona.api_client.model.agent import Agent
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
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent

    # example passing only required values which don't have defaults set
    try:
        # Information about agents for a specific class
        api_response = api_instance.get_agents_by_class(agent_class)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agents_by_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |

### Return type

[**[Agent]**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of agents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_by_class**
> put_agent_by_class(agent_class, agent)

Create or update an agent for a specific class

Create a new agent or update an agent if already exists

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import agents_api
from eliona.api_client.model.agent import Agent
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
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent = Agent(
        node_id="1234",
        asset_id=4711,
        description="IOSYS Agent east plant",
        enable=False,
        config={},
    ) # Agent | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an agent for a specific class
        api_instance.put_agent_by_class(agent_class, agent)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_by_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent** | [**Agent**](Agent.md)|  |

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
**200** | Successfully created a new or updated an existing agent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_by_id**
> put_agent_device_by_id(agent_class, agent_id, agent_device)

Create or update an agent device

Create a new agent device or update an agent device if already exists

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import agents_api
from eliona.api_client.model.agent_device import AgentDevice
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
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_id = 4711 # int | The id of the agent
    agent_device = AgentDevice(None) # AgentDevice | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an agent device
        api_instance.put_agent_device_by_id(agent_class, agent_id, agent_device)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_id** | **int**| The id of the agent |
 **agent_device** | [**AgentDevice**](AgentDevice.md)|  |

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
**200** | Successfully created a new or updated an existing agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_mapping_by_id**
> AgentDeviceMapping put_agent_device_mapping_by_id(agent_class, agent_device_id, agent_device_mapping)

Create or update an agent device mapping

Create a new agent device mapping or update an agent device mapping if already exists

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import agents_api
from eliona.api_client.model.agent_device_mapping import AgentDeviceMapping
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
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device
    agent_device_mapping = AgentDeviceMapping(None) # AgentDeviceMapping | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an agent device mapping
        api_response = api_instance.put_agent_device_mapping_by_id(agent_class, agent_device_id, agent_device_mapping)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_mapping_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_device_id** | **int**| The id of the device |
 **agent_device_mapping** | [**AgentDeviceMapping**](AgentDeviceMapping.md)|  |

### Return type

[**AgentDeviceMapping**](AgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing agent device mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


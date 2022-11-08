# eliona.api_client.AgentsApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_by_class_and_id**](AgentsApi.md#get_agent_by_class_and_id) | **GET** /agents/{agent-class}/{agent-id} | Information about an agent
[**get_agent_device_by_id**](AgentsApi.md#get_agent_device_by_id) | **GET** /agent-devices/{agent-class}/{agent-device-id} | Information about agent device
[**get_agent_device_mapping_by_id**](AgentsApi.md#get_agent_device_mapping_by_id) | **GET** /agent-device-mappings/{agent-class}/{agent-device-mapping-id} | Information about agent device mapping
[**get_agent_device_mappings_by_device_id**](AgentsApi.md#get_agent_device_mappings_by_device_id) | **GET** /agent-devices/{agent-class}/{agent-device-id}/mappings | Information about agent device mappings
[**get_agent_devices_by_agent_id**](AgentsApi.md#get_agent_devices_by_agent_id) | **GET** /agents/{agent-class}/{agent-id}/devices | Information about agent devices
[**get_agents**](AgentsApi.md#get_agents) | **GET** /agents | Information about agents
[**get_agents_by_class**](AgentsApi.md#get_agents_by_class) | **GET** /agents/{agent-class} | Information about agents for a specific class
[**post_agent_by_class**](AgentsApi.md#post_agent_by_class) | **POST** /agents/{agent-class} | Create an agent
[**post_agent_device_by_agent_id**](AgentsApi.md#post_agent_device_by_agent_id) | **POST** /agents/{agent-class}/{agent-id}/devices | Create an agent device
[**post_agent_device_mapping_by_device_id**](AgentsApi.md#post_agent_device_mapping_by_device_id) | **POST** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create an agent device mapping
[**put_agent_by_class**](AgentsApi.md#put_agent_by_class) | **PUT** /agents/{agent-class} | Create or update an agent
[**put_agent_by_class_and_id**](AgentsApi.md#put_agent_by_class_and_id) | **PUT** /agents/{agent-class}/{agent-id} | Update an agent
[**put_agent_device_by_agent_id**](AgentsApi.md#put_agent_device_by_agent_id) | **PUT** /agents/{agent-class}/{agent-id}/devices | Create or update an agent device
[**put_agent_device_by_id**](AgentsApi.md#put_agent_device_by_id) | **PUT** /agent-devices/{agent-class}/{agent-device-id} | Update an agent device
[**put_agent_device_mapping_by_device_id**](AgentsApi.md#put_agent_device_mapping_by_device_id) | **PUT** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create or update an agent device mapping
[**put_agent_device_mapping_by_id**](AgentsApi.md#put_agent_device_mapping_by_id) | **PUT** /agent-device-mappings/{agent-class}/{agent-device-mapping-id} | Update an agent device mapping


# **get_agent_by_class_and_id**
> Agent get_agent_by_class_and_id(agent_id, agent_class)

Information about an agent

Gets information about an agent.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_id = 4711 # int | The id of the agent
    agent_class = "iosys" # str | The class of an agent

    # example passing only required values which don't have defaults set
    try:
        # Information about an agent
        api_response = api_instance.get_agent_by_class_and_id(agent_id, agent_class)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_by_class_and_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| The id of the agent |
 **agent_class** | **str**| The class of an agent |

### Return type

[**Agent**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an agent |  -  |
**404** | Agent with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_device_by_id**
> [AgentDevice] get_agent_device_by_id(agent_class, agent_device_id)

Information about agent device

Gets information about agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device

    # example passing only required values which don't have defaults set
    try:
        # Information about agent device
        api_response = api_instance.get_agent_device_by_id(agent_class, agent_device_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_device_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_device_id** | **int**| The id of the device |

### Return type

[**[AgentDevice]**](AgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_device_mapping_by_id**
> [AgentDeviceMapping] get_agent_device_mapping_by_id(agent_class, agent_device_mapping_id)

Information about agent device mapping

Gets information about agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_mapping_id = 4711 # int | The id of the device mapping

    # example passing only required values which don't have defaults set
    try:
        # Information about agent device mapping
        api_response = api_instance.get_agent_device_mapping_by_id(agent_class, agent_device_mapping_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_device_mapping_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_device_mapping_id** | **int**| The id of the device mapping |

### Return type

[**[AgentDeviceMapping]**](AgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_device_mappings_by_device_id**
> [AgentDeviceMapping] get_agent_device_mappings_by_device_id(agent_class, agent_device_id)

Information about agent device mappings

Gets information about mappings between agent and eliona.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device

    # example passing only required values which don't have defaults set
    try:
        # Information about agent device mappings
        api_response = api_instance.get_agent_device_mappings_by_device_id(agent_class, agent_device_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_device_mappings_by_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_device_id** | **int**| The id of the device |

### Return type

[**[AgentDeviceMapping]**](AgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_devices_by_agent_id**
> [AgentDevice] get_agent_devices_by_agent_id(agent_class, agent_id)

Information about agent devices

Gets information about agent devices.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_id = 4711 # int | The id of the agent

    # example passing only required values which don't have defaults set
    try:
        # Information about agent devices
        api_response = api_instance.get_agent_devices_by_agent_id(agent_class, agent_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_devices_by_agent_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_id** | **int**| The id of the agent |

### Return type

[**[AgentDevice]**](AgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

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
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

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
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of agents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_by_class**
> Agent post_agent_by_class(agent_class, agent)

Create an agent

Create a new agent for a specific class

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        # Create an agent
        api_response = api_instance.post_agent_by_class(agent_class, agent)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->post_agent_by_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent** | [**Agent**](Agent.md)|  |

### Return type

[**Agent**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new agent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_device_by_agent_id**
> AgentDevice post_agent_device_by_agent_id(agent_class, agent_id, agent_device)

Create an agent device

Create a new agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_id = 4711 # int | The id of the agent
    agent_device = AgentDevice(None) # AgentDevice | 

    # example passing only required values which don't have defaults set
    try:
        # Create an agent device
        api_response = api_instance.post_agent_device_by_agent_id(agent_class, agent_id, agent_device)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->post_agent_device_by_agent_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_id** | **int**| The id of the agent |
 **agent_device** | [**AgentDevice**](AgentDevice.md)|  |

### Return type

[**AgentDevice**](AgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_device_mapping_by_device_id**
> AgentDeviceMapping post_agent_device_mapping_by_device_id(agent_class, agent_device_id, agent_device_mapping)

Create an agent device mapping

Create a new agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device
    agent_device_mapping = AgentDeviceMapping(None) # AgentDeviceMapping | 

    # example passing only required values which don't have defaults set
    try:
        # Create an agent device mapping
        api_response = api_instance.post_agent_device_mapping_by_device_id(agent_class, agent_device_id, agent_device_mapping)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->post_agent_device_mapping_by_device_id: %s\n" % e)
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new agent device mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_by_class**
> Agent put_agent_by_class(agent_class, agent)

Create or update an agent

Deprecated - use POST /agents/{agent-class} for creating and PUT /agents/{agent-class}/{agent-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        # Create or update an agent
        api_response = api_instance.put_agent_by_class(agent_class, agent)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_by_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent** | [**Agent**](Agent.md)|  |

### Return type

[**Agent**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing agent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_by_class_and_id**
> Agent put_agent_by_class_and_id(agent_id, agent_class, agent)

Update an agent

Update an agent.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_id = 4711 # int | The id of the agent
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
        # Update an agent
        api_response = api_instance.put_agent_by_class_and_id(agent_id, agent_class, agent)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_by_class_and_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| The id of the agent |
 **agent_class** | **str**| The class of an agent |
 **agent** | [**Agent**](Agent.md)|  |

### Return type

[**Agent**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing agent |  -  |
**404** | Agent with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_by_agent_id**
> AgentDevice put_agent_device_by_agent_id(agent_class, agent_id, agent_device)

Create or update an agent device

Deprecated - use POST /agents/{agent-class}/{agent-id}/devices for creating and PUT /agent-devices/{agent-class}/{agent-device-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.put_agent_device_by_agent_id(agent_class, agent_id, agent_device)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_by_agent_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_id** | **int**| The id of the agent |
 **agent_device** | [**AgentDevice**](AgentDevice.md)|  |

### Return type

[**AgentDevice**](AgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_by_id**
> AgentDevice put_agent_device_by_id(agent_class, agent_device_id, agent_device)

Update an agent device

Update a new agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device
    agent_device = AgentDevice(None) # AgentDevice | 

    # example passing only required values which don't have defaults set
    try:
        # Update an agent device
        api_response = api_instance.put_agent_device_by_id(agent_class, agent_device_id, agent_device)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_device_id** | **int**| The id of the device |
 **agent_device** | [**AgentDevice**](AgentDevice.md)|  |

### Return type

[**AgentDevice**](AgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully update a new agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_mapping_by_device_id**
> AgentDeviceMapping put_agent_device_mapping_by_device_id(agent_class, agent_device_id, agent_device_mapping)

Create or update an agent device mapping

Deprecated - Use POST /agent-devices/{agent-class}/{agent-device-id}/mappings for creating and /agent-device-mappings/{agent-class}/{agent-device-mapping-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.put_agent_device_mapping_by_device_id(agent_class, agent_device_id, agent_device_mapping)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_mapping_by_device_id: %s\n" % e)
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing agent device mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_mapping_by_id**
> AgentDeviceMapping put_agent_device_mapping_by_id(agent_class, agent_device_mapping_id, agent_device_mapping)

Update an agent device mapping

Update a new agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_mapping_id = 4711 # int | The id of the device mapping
    agent_device_mapping = AgentDeviceMapping(None) # AgentDeviceMapping | 

    # example passing only required values which don't have defaults set
    try:
        # Update an agent device mapping
        api_response = api_instance.put_agent_device_mapping_by_id(agent_class, agent_device_mapping_id, agent_device_mapping)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_mapping_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent |
 **agent_device_mapping_id** | **int**| The id of the device mapping |
 **agent_device_mapping** | [**AgentDeviceMapping**](AgentDeviceMapping.md)|  |

### Return type

[**AgentDeviceMapping**](AgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully update a new agent device mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


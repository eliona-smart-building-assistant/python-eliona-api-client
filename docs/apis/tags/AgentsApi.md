<a name="__pageTop"></a>
# eliona.api_client.apis.tags.agents_api.AgentsApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_by_class_and_id**](#get_agent_by_class_and_id) | **get** /agents/{agent-class}/{agent-id} | Information about an agent
[**get_agent_device_by_id**](#get_agent_device_by_id) | **get** /agent-devices/{agent-class}/{agent-device-id} | Information about agent device
[**get_agent_device_mapping_by_id**](#get_agent_device_mapping_by_id) | **get** /agent-device-mappings/{agent-class}/{agent-device-mapping-id} | Information about agent device mapping
[**get_agent_device_mappings_by_device_id**](#get_agent_device_mappings_by_device_id) | **get** /agent-devices/{agent-class}/{agent-device-id}/mappings | Information about agent device mappings
[**get_agent_devices_by_agent_id**](#get_agent_devices_by_agent_id) | **get** /agents/{agent-class}/{agent-id}/devices | Information about agent devices
[**get_agents**](#get_agents) | **get** /agents | Information about agents
[**get_agents_by_class**](#get_agents_by_class) | **get** /agents/{agent-class} | Information about agents for a specific class
[**post_agent_by_class**](#post_agent_by_class) | **post** /agents/{agent-class} | Create an agent
[**post_agent_device_by_agent_id**](#post_agent_device_by_agent_id) | **post** /agents/{agent-class}/{agent-id}/devices | Create an agent device
[**post_agent_device_mapping_by_device_id**](#post_agent_device_mapping_by_device_id) | **post** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create an agent device mapping
[**put_agent_by_class**](#put_agent_by_class) | **put** /agents/{agent-class} | Create or update an agent
[**put_agent_by_class_and_id**](#put_agent_by_class_and_id) | **put** /agents/{agent-class}/{agent-id} | Update an agent
[**put_agent_device_by_agent_id**](#put_agent_device_by_agent_id) | **put** /agents/{agent-class}/{agent-id}/devices | Create or update an agent device
[**put_agent_device_by_id**](#put_agent_device_by_id) | **put** /agent-devices/{agent-class}/{agent-device-id} | Update an agent device
[**put_agent_device_mapping_by_device_id**](#put_agent_device_mapping_by_device_id) | **put** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create or update an agent device mapping
[**put_agent_device_mapping_by_id**](#put_agent_device_mapping_by_id) | **put** /agent-device-mappings/{agent-class}/{agent-device-mapping-id} | Update an agent device mapping

# **get_agent_by_class_and_id**
<a name="get_agent_by_class_and_id"></a>
> Agent get_agent_by_class_and_id(agent_idagent_class)

Information about an agent

Gets information about an agent.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent import Agent
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-id': 4711,
        'agent-class': "iosys",
    }
    try:
        # Information about an agent
        api_response = api_instance.get_agent_by_class_and_id(
            path_params=path_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_by_class_and_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-id | AgentIdSchema | | 
agent-class | AgentClassSchema | | 

# AgentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_agent_by_class_and_id.ApiResponseFor200) | Successfully returned an agent
404 | [ApiResponseFor404](#get_agent_by_class_and_id.ApiResponseFor404) | Agent with id not found

#### get_agent_by_class_and_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Agent**](../../models/Agent.md) |  | 


#### get_agent_by_class_and_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_agent_device_by_id**
<a name="get_agent_device_by_id"></a>
> [AgentDevice] get_agent_device_by_id(agent_classagent_device_id)

Information about agent device

Gets information about agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device import AgentDevice
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-device-id': 4711,
    }
    try:
        # Information about agent device
        api_response = api_instance.get_agent_device_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_device_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-device-id | AgentDeviceIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentDeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_agent_device_by_id.ApiResponseFor200) | Successfully returned a agent device

#### get_agent_device_by_id.ApiResponseFor200
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
[**AgentDevice**]({{complexTypePrefix}}AgentDevice.md) | [**AgentDevice**]({{complexTypePrefix}}AgentDevice.md) | [**AgentDevice**]({{complexTypePrefix}}AgentDevice.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_agent_device_mapping_by_id**
<a name="get_agent_device_mapping_by_id"></a>
> [AgentDeviceMapping] get_agent_device_mapping_by_id(agent_classagent_device_mapping_id)

Information about agent device mapping

Gets information about agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device_mapping import AgentDeviceMapping
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-device-mapping-id': 4711,
    }
    try:
        # Information about agent device mapping
        api_response = api_instance.get_agent_device_mapping_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_device_mapping_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-device-mapping-id | AgentDeviceMappingIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentDeviceMappingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_agent_device_mapping_by_id.ApiResponseFor200) | Successfully returned a agent device

#### get_agent_device_mapping_by_id.ApiResponseFor200
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
[**AgentDeviceMapping**]({{complexTypePrefix}}AgentDeviceMapping.md) | [**AgentDeviceMapping**]({{complexTypePrefix}}AgentDeviceMapping.md) | [**AgentDeviceMapping**]({{complexTypePrefix}}AgentDeviceMapping.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_agent_device_mappings_by_device_id**
<a name="get_agent_device_mappings_by_device_id"></a>
> [AgentDeviceMapping] get_agent_device_mappings_by_device_id(agent_classagent_device_id)

Information about agent device mappings

Gets information about mappings between agent and eliona.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device_mapping import AgentDeviceMapping
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-device-id': 4711,
    }
    try:
        # Information about agent device mappings
        api_response = api_instance.get_agent_device_mappings_by_device_id(
            path_params=path_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_device_mappings_by_device_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-device-id | AgentDeviceIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentDeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_agent_device_mappings_by_device_id.ApiResponseFor200) | Successfully returned a mapping

#### get_agent_device_mappings_by_device_id.ApiResponseFor200
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
[**AgentDeviceMapping**]({{complexTypePrefix}}AgentDeviceMapping.md) | [**AgentDeviceMapping**]({{complexTypePrefix}}AgentDeviceMapping.md) | [**AgentDeviceMapping**]({{complexTypePrefix}}AgentDeviceMapping.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_agent_devices_by_agent_id**
<a name="get_agent_devices_by_agent_id"></a>
> [AgentDevice] get_agent_devices_by_agent_id(agent_classagent_id)

Information about agent devices

Gets information about agent devices.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device import AgentDevice
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-id': 4711,
    }
    try:
        # Information about agent devices
        api_response = api_instance.get_agent_devices_by_agent_id(
            path_params=path_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_devices_by_agent_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-id | AgentIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_agent_devices_by_agent_id.ApiResponseFor200) | Successfully returned a list of devices

#### get_agent_devices_by_agent_id.ApiResponseFor200
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
[**AgentDevice**]({{complexTypePrefix}}AgentDevice.md) | [**AgentDevice**]({{complexTypePrefix}}AgentDevice.md) | [**AgentDevice**]({{complexTypePrefix}}AgentDevice.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_agents**
<a name="get_agents"></a>
> [Agent] get_agents()

Information about agents

Gets information about agents.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent import Agent
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_agents.ApiResponseFor200) | Successfully returned a list of agents

#### get_agents.ApiResponseFor200
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
[**Agent**]({{complexTypePrefix}}Agent.md) | [**Agent**]({{complexTypePrefix}}Agent.md) | [**Agent**]({{complexTypePrefix}}Agent.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_agents_by_class**
<a name="get_agents_by_class"></a>
> [Agent] get_agents_by_class(agent_class)

Information about agents for a specific class

Gets information about agents.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent import Agent
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
    }
    try:
        # Information about agents for a specific class
        api_response = api_instance.get_agents_by_class(
            path_params=path_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agents_by_class: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_agents_by_class.ApiResponseFor200) | Successfully returned a list of agents

#### get_agents_by_class.ApiResponseFor200
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
[**Agent**]({{complexTypePrefix}}Agent.md) | [**Agent**]({{complexTypePrefix}}Agent.md) | [**Agent**]({{complexTypePrefix}}Agent.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_agent_by_class**
<a name="post_agent_by_class"></a>
> Agent post_agent_by_class(agent_classagent)

Create an agent

Create a new agent for a specific class

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent import Agent
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
    }
    body = Agent(
        id=4711,
        node_id="1234",
        asset_id=4711,
        _class=AgentClass("iosys"),
        description="IOSYS Agent east plant",
        enable=False,
        config=dict(),
    )
    try:
        # Create an agent
        api_response = api_instance.post_agent_by_class(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->post_agent_by_class: %s\n" % e)
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
[**Agent**](../../models/Agent.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_agent_by_class.ApiResponseFor201) | Successfully created a new agent

#### post_agent_by_class.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Agent**](../../models/Agent.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_agent_device_by_agent_id**
<a name="post_agent_device_by_agent_id"></a>
> AgentDevice post_agent_device_by_agent_id(agent_classagent_idagent_device)

Create an agent device

Create a new agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device import AgentDevice
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-id': 4711,
    }
    body = AgentDevice(None)
    try:
        # Create an agent device
        api_response = api_instance.post_agent_device_by_agent_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->post_agent_device_by_agent_id: %s\n" % e)
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
[**AgentDevice**](../../models/AgentDevice.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-id | AgentIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_agent_device_by_agent_id.ApiResponseFor201) | Successfully created a new agent device

#### post_agent_device_by_agent_id.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentDevice**](../../models/AgentDevice.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_agent_device_mapping_by_device_id**
<a name="post_agent_device_mapping_by_device_id"></a>
> AgentDeviceMapping post_agent_device_mapping_by_device_id(agent_classagent_device_idagent_device_mapping)

Create an agent device mapping

Create a new agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device_mapping import AgentDeviceMapping
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-device-id': 4711,
    }
    body = AgentDeviceMapping(None)
    try:
        # Create an agent device mapping
        api_response = api_instance.post_agent_device_mapping_by_device_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->post_agent_device_mapping_by_device_id: %s\n" % e)
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
[**AgentDeviceMapping**](../../models/AgentDeviceMapping.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-device-id | AgentDeviceIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentDeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_agent_device_mapping_by_device_id.ApiResponseFor201) | Successfully created a new agent device mapping

#### post_agent_device_mapping_by_device_id.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentDeviceMapping**](../../models/AgentDeviceMapping.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_agent_by_class**
<a name="put_agent_by_class"></a>
> Agent put_agent_by_class(agent_classagent)

Create or update an agent

Deprecated - use POST /agents/{agent-class} for creating and PUT /agents/{agent-class}/{agent-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent import Agent
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
    }
    body = Agent(
        id=4711,
        node_id="1234",
        asset_id=4711,
        _class=AgentClass("iosys"),
        description="IOSYS Agent east plant",
        enable=False,
        config=dict(),
    )
    try:
        # Create or update an agent
        api_response = api_instance.put_agent_by_class(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_by_class: %s\n" % e)
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
[**Agent**](../../models/Agent.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_agent_by_class.ApiResponseFor200) | Successfully created a new or updated an existing agent

#### put_agent_by_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Agent**](../../models/Agent.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_agent_by_class_and_id**
<a name="put_agent_by_class_and_id"></a>
> Agent put_agent_by_class_and_id(agent_idagent_classagent)

Update an agent

Update an agent.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent import Agent
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-id': 4711,
        'agent-class': "iosys",
    }
    body = Agent(
        id=4711,
        node_id="1234",
        asset_id=4711,
        _class=AgentClass("iosys"),
        description="IOSYS Agent east plant",
        enable=False,
        config=dict(),
    )
    try:
        # Update an agent
        api_response = api_instance.put_agent_by_class_and_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_by_class_and_id: %s\n" % e)
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
[**Agent**](../../models/Agent.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-id | AgentIdSchema | | 
agent-class | AgentClassSchema | | 

# AgentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_agent_by_class_and_id.ApiResponseFor200) | Successfully updated an existing agent
404 | [ApiResponseFor404](#put_agent_by_class_and_id.ApiResponseFor404) | Agent with id not found

#### put_agent_by_class_and_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Agent**](../../models/Agent.md) |  | 


#### put_agent_by_class_and_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_agent_device_by_agent_id**
<a name="put_agent_device_by_agent_id"></a>
> AgentDevice put_agent_device_by_agent_id(agent_classagent_idagent_device)

Create or update an agent device

Deprecated - use POST /agents/{agent-class}/{agent-id}/devices for creating and PUT /agent-devices/{agent-class}/{agent-device-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device import AgentDevice
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-id': 4711,
    }
    body = AgentDevice(None)
    try:
        # Create or update an agent device
        api_response = api_instance.put_agent_device_by_agent_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_by_agent_id: %s\n" % e)
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
[**AgentDevice**](../../models/AgentDevice.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-id | AgentIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_agent_device_by_agent_id.ApiResponseFor200) | Successfully created a new or updated an existing agent device

#### put_agent_device_by_agent_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentDevice**](../../models/AgentDevice.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_agent_device_by_id**
<a name="put_agent_device_by_id"></a>
> AgentDevice put_agent_device_by_id(agent_classagent_device_idagent_device)

Update an agent device

Update a new agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device import AgentDevice
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-device-id': 4711,
    }
    body = AgentDevice(None)
    try:
        # Update an agent device
        api_response = api_instance.put_agent_device_by_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_by_id: %s\n" % e)
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
[**AgentDevice**](../../models/AgentDevice.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-device-id | AgentDeviceIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentDeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_agent_device_by_id.ApiResponseFor200) | Successfully update a new agent device

#### put_agent_device_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentDevice**](../../models/AgentDevice.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_agent_device_mapping_by_device_id**
<a name="put_agent_device_mapping_by_device_id"></a>
> AgentDeviceMapping put_agent_device_mapping_by_device_id(agent_classagent_device_idagent_device_mapping)

Create or update an agent device mapping

Deprecated - Use POST /agent-devices/{agent-class}/{agent-device-id}/mappings for creating and /agent-device-mappings/{agent-class}/{agent-device-mapping-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device_mapping import AgentDeviceMapping
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-device-id': 4711,
    }
    body = AgentDeviceMapping(None)
    try:
        # Create or update an agent device mapping
        api_response = api_instance.put_agent_device_mapping_by_device_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_mapping_by_device_id: %s\n" % e)
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
[**AgentDeviceMapping**](../../models/AgentDeviceMapping.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-device-id | AgentDeviceIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentDeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_agent_device_mapping_by_device_id.ApiResponseFor200) | Successfully created a new or updated an existing agent device mapping

#### put_agent_device_mapping_by_device_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentDeviceMapping**](../../models/AgentDeviceMapping.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_agent_device_mapping_by_id**
<a name="put_agent_device_mapping_by_id"></a>
> AgentDeviceMapping put_agent_device_mapping_by_id(agent_classagent_device_mapping_idagent_device_mapping)

Update an agent device mapping

Update a new agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import agents_api
from eliona/api_client.model.agent_device_mapping import AgentDeviceMapping
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

    # example passing only required values which don't have defaults set
    path_params = {
        'agent-class': "iosys",
        'agent-device-mapping-id': 4711,
    }
    body = AgentDeviceMapping(None)
    try:
        # Update an agent device mapping
        api_response = api_instance.put_agent_device_mapping_by_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->put_agent_device_mapping_by_id: %s\n" % e)
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
[**AgentDeviceMapping**](../../models/AgentDeviceMapping.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
agent-class | AgentClassSchema | | 
agent-device-mapping-id | AgentDeviceMappingIdSchema | | 

# AgentClassSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["iosys", "mbus", ] 

# AgentDeviceMappingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_agent_device_mapping_by_id.ApiResponseFor200) | Successfully update a new agent device mapping

#### put_agent_device_mapping_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentDeviceMapping**](../../models/AgentDeviceMapping.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


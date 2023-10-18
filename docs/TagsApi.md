# eliona.api_client.TagsApi

All URIs are relative to *https://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tag_by_name**](TagsApi.md#get_tag_by_name) | **GET** /tags/{tag-name} | Information about a tag
[**get_tags**](TagsApi.md#get_tags) | **GET** /tags | Information about tags
[**put_tag**](TagsApi.md#put_tag) | **PUT** /tags | Create or update a tag


# **get_tag_by_name**
> Tag get_tag_by_name(tag_name)

Information about a tag

Gets information about a tag.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import tags_api
from eliona.api_client.model.tag import Tag
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
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
    api_instance = tags_api.TagsApi(api_client)
    tag_name = "Support" # str | The name of the tag

    # example passing only required values which don't have defaults set
    try:
        # Information about a tag
        api_response = api_instance.get_tag_by_name(tag_name)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling TagsApi->get_tag_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The name of the tag |

### Return type

[**Tag**](Tag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the tag by name. |  -  |
**404** | Tag with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> [Tag] get_tags()

Information about tags

Gets a list of tags

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import tags_api
from eliona.api_client.model.tag import Tag
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
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
    api_instance = tags_api.TagsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Information about tags
        api_response = api_instance.get_tags()
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling TagsApi->get_tags: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Tag]**](Tag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of tags |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tag**
> Tag put_tag(tag)

Create or update a tag

Creates a tag if no tag exists or update it if already exists. Uses name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import tags_api
from eliona.api_client.model.tag import Tag
from pprint import pprint
# Defining the host is optional and defaults to https://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://api.eliona.io/v2"
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
    api_instance = tags_api.TagsApi(api_client)
    tag = Tag(
        name="Support",
        color_id=3,
        custom=True,
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update a tag
        api_response = api_instance.put_tag(tag)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling TagsApi->put_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**Tag**](Tag.md)|  |

### Return type

[**Tag**](Tag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing tag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


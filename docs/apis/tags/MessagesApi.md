<a name="__pageTop"></a>
# eliona.api_client.apis.tags.messages_api.MessagesApi

All URIs are relative to *http://api.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message_receipt_by_id**](#get_message_receipt_by_id) | **get** /message-receipts/{message-id} | Information about a message
[**post_mail**](#post_mail) | **post** /send-mail | Send e-mail

# **get_message_receipt_by_id**
<a name="get_message_receipt_by_id"></a>
> MessageReceipt get_message_receipt_by_id(message_id)

Information about a message

Gets receipt information for a message.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import messages_api
from eliona/api_client.model.message_receipt import MessageReceipt
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
    api_instance = messages_api.MessagesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'message-id': "AB0815",
    }
    try:
        # Information about a message
        api_response = api_instance.get_message_receipt_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling MessagesApi->get_message_receipt_by_id: %s\n" % e)
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
message-id | MessageIdSchema | | 

# MessageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_message_receipt_by_id.ApiResponseFor200) | Successfully returned the receipt
404 | [ApiResponseFor404](#get_message_receipt_by_id.ApiResponseFor404) | Message with id not found

#### get_message_receipt_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageReceipt**](../../models/MessageReceipt.md) |  | 


#### get_message_receipt_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_mail**
<a name="post_mail"></a>
> MessageReceipt post_mail(message)

Send e-mail

Sends an e-mail to recipients

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import eliona.api_client
from eliona.api_client.apis.tags import messages_api
from eliona/api_client.model.message import Message
from eliona/api_client.model.message_receipt import MessageReceipt
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
    api_instance = messages_api.MessagesApi(api_client)

    # example passing only required values which don't have defaults set
    body = Message(
        sender="sender@example.com",
        recipients=[
            "recipient@example.com"
        ],
        copy_recipients=[
            "copy-recipient@example.com"
        ],
        blind_copy_recipients=[
            "blind-copy-recipient@example.com"
        ],
        subject="This is a example message",
        content="<h1>Example</h1>",
        attachments=[
            Attachment(
                name="example.gif",
                content_type="image/png",
                encoding="base64",
                content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
            )
        ],
    )
    try:
        # Send e-mail
        api_response = api_instance.post_mail(
            body=body,
        )
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling MessagesApi->post_mail: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Message**](../../models/Message.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_mail.ApiResponseFor201) | Successfully accepted the e-mail

#### post_mail.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageReceipt**](../../models/MessageReceipt.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [BearerAuth](../../../README.md#BearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


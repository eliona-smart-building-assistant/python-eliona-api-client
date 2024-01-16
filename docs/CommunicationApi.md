# eliona.api_client.CommunicationApi

All URIs are relative to *https://name.eliona.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message_receipt_by_id**](CommunicationApi.md#get_message_receipt_by_id) | **GET** /message-receipts/{message-id} | Information about a message
[**post_mail**](CommunicationApi.md#post_mail) | **POST** /send-mail | Send e-mail
[**post_notification**](CommunicationApi.md#post_notification) | **POST** /send-notification | Send notification


# **get_message_receipt_by_id**
> MessageReceipt get_message_receipt_by_id(message_id)

Information about a message

Gets receipt information for a message.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import communication_api
from eliona.api_client.model.message_receipt import MessageReceipt
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
    api_instance = communication_api.CommunicationApi(api_client)
    message_id = "AB0815" # str | The id of the message

    # example passing only required values which don't have defaults set
    try:
        # Information about a message
        api_response = api_instance.get_message_receipt_by_id(message_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling CommunicationApi->get_message_receipt_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| The id of the message |

### Return type

[**MessageReceipt**](MessageReceipt.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the receipt |  -  |
**404** | Message with ID not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mail**
> MessageReceipt post_mail(message)

Send e-mail

Sends an e-mail to recipients

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import communication_api
from eliona.api_client.model.message_receipt import MessageReceipt
from eliona.api_client.model.message import Message
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
    api_instance = communication_api.CommunicationApi(api_client)
    message = Message(
        sender="sender@example.com",
        recipients=[
            "recipient@example.com",
        ],
        copy_recipients=[
            "copy-recipient@example.com",
        ],
        blind_copy_recipients=[
            "blind-copy-recipient@example.com",
        ],
        subject="This is a example message",
        content="<h1>Example</h1>",
        attachments=[
            Attachment(
                name="example.gif",
                content_type="image/png",
                encoding="base64",
                content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
            ),
        ],
    ) # Message | 

    # example passing only required values which don't have defaults set
    try:
        # Send e-mail
        api_response = api_instance.post_mail(message)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling CommunicationApi->post_mail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | [**Message**](Message.md)|  |

### Return type

[**MessageReceipt**](MessageReceipt.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully accepted the e-mail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_notification**
> MessageReceipt post_notification(notification)

Send notification

Sends a notification to Eliona users

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import communication_api
from eliona.api_client.model.notification import Notification
from eliona.api_client.model.message_receipt import MessageReceipt
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
    api_instance = communication_api.CommunicationApi(api_client)
    notification = Notification(
        user="peter.fox@example.com",
        project_id="99",
        message=Translation(
            de="Das ist ein deutscher Text",
            en="This is an english text",
            fr="Ceci est en texte anglais",
            it="Questo è nel testo inglese",
        ),
    ) # Notification | 

    # example passing only required values which don't have defaults set
    try:
        # Send notification
        api_response = api_instance.post_notification(notification)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling CommunicationApi->post_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | [**Notification**](Notification.md)|  |

### Return type

[**MessageReceipt**](MessageReceipt.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully accepted the notification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# eliona.api_client.model.message.Message

A message

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A message | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[recipients](#recipients)** | list, tuple,  | tuple,  | A list of recipient addresses to receive this message | 
**content** | str,  | str,  | The content of the message | 
**sender** | None, str,  | NoneClass, str,  | Address of the sender, e.g. an e-mail address | [optional] 
**[copyRecipients](#copyRecipients)** | list, tuple, None,  | tuple, NoneClass,  | A list of recipient addresses to receive this message as copy | [optional] 
**[blindCopyRecipients](#blindCopyRecipients)** | list, tuple, None,  | tuple, NoneClass,  | A list of recipient addresses to receive this message as blind copy without any other recipient information | [optional] 
**subject** | str,  | str,  | The subject for this message | [optional] 
**mimeType** | None, str,  | NoneClass, str,  | The MIME type of the message content | [optional] 
**[attachments](#attachments)** | list, tuple, None,  | tuple, NoneClass,  | A list of files attached to the message | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# recipients

A list of recipient addresses to receive this message

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of recipient addresses to receive this message | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | A recipient&#x27;s address, e.g. an e-mail address | 

# copyRecipients

A list of recipient addresses to receive this message as copy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A list of recipient addresses to receive this message as copy | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | A recipient&#x27;s address, e.g. an e-mail address | 

# blindCopyRecipients

A list of recipient addresses to receive this message as blind copy without any other recipient information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A list of recipient addresses to receive this message as blind copy without any other recipient information | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | A recipient&#x27;s address, e.g. an e-mail address | 

# attachments

A list of files attached to the message

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A list of files attached to the message | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Attachment**](Attachment.md) | [**Attachment**](Attachment.md) | [**Attachment**](Attachment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


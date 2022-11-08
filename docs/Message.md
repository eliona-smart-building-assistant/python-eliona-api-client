# Message

A message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **[str]** | A list of recipient addresses to receive this message | 
**content** | **str** | The content of the message. If template is used, the content is embedded in the template. | 
**sender** | **str, none_type** | Address of the sender, e.g. an e-mail address | [optional] 
**copy_recipients** | **[str], none_type** | A list of recipient addresses to receive this message as copy | [optional] 
**blind_copy_recipients** | **[str], none_type** | A list of recipient addresses to receive this message as blind copy without any other recipient information | [optional] 
**subject** | **str** | The subject for this message | [optional] 
**attachments** | [**[Attachment], none_type**](Attachment.md) | A list of files attached to the message | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



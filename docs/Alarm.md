# Alarm

An alarm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**HeapSubtype**](HeapSubtype.md) |  | 
**priority** | [**AlarmPriority**](AlarmPriority.md) |  | 
**timestamp** | **datetime** | Timestamp of the latest data change | 
**occurrences** | **int** | How often this alarm is triggered | 
**rule_id** | **int, none_type** | The id of the corresponding rule | [optional] 
**attribute** | **str, none_type** | Name of the attribute of the asset type | [optional] 
**requires_acknowledge** | **bool** | Requires the alarm an acknowledgment | [optional]  if omitted the server will use the default value of False
**value** | **float, none_type** | The value which triggers the alarm | [optional] 
**gone_timestamp** | **datetime, none_type** | Timestamp of the latest data change | [optional] 
**acknowledge_timestamp** | **datetime, none_type** | Timestamp of the latest data change | [optional] 
**acknowledge_text** | **str, none_type** | Text of acknowledgement | [optional] 
**acknowledge_user_id** | **str, none_type** | User who acknowledged the alarm | [optional] 
**message** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Message texts for alarm | [optional] 
**asset_info** | [**Asset**](Asset.md) |  | [optional] 
**rule_info** | [**AlarmRule**](AlarmRule.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



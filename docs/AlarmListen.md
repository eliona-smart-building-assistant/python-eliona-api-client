# AlarmListen


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **int** | The id of the corresponding rule | [readonly] 
**message** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Message.yaml texts for alarm | 
**status_code** | **int** | The status code expecting when actually perform the operation. Some values are - 200: updated (ok)  - 201: created - 204: deleted (no content) - 304: unchanged (not modified) - 400: problem (bad request) - 404: not found - 409: duplicated (conflict) - 422: unprocessable  | [optional] 
**asset_id** | **int, none_type** | ID of the corresponding asset | [optional] [readonly] 
**subtype** | **str, none_type** | Type of asset data | [optional] [readonly] 
**attribute** | **str, none_type** | Name of the attribute of the asset type | [optional] [readonly] 
**priority** | **int, none_type** | The priority of the alarm. The lower this value the higher the priority. | [optional] 
**requires_acknowledge** | **bool, none_type** | Requires the alarm an acknowledgment | [optional]  if omitted the server will use the default value of False
**value** | **float, none_type** | The value which triggers the alarm | [optional] 
**timestamp** | **datetime, none_type** | Timestamp of the latest data change | [optional] 
**gone_timestamp** | **datetime, none_type** | Timestamp of the latest data change | [optional] [readonly] 
**acknowledge_timestamp** | **datetime, none_type** | Timestamp of the latest data change | [optional] [readonly] 
**occurrences** | **int, none_type** | How often this alarm is triggered | [optional] [readonly] 
**acknowledge_text** | **str, none_type** | Text of acknowledgement | [optional] [readonly] 
**acknowledge_user_id** | **str, none_type** | User who acknowledged the alarm | [optional] [readonly] 
**asset_info** | [**Asset**](Asset.md) |  | [optional] 
**rule_info** | [**AlarmRule**](AlarmRule.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



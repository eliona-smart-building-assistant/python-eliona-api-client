# eliona.api_client.model.alarm.Alarm

An alarm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | An alarm | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**occurrences** | decimal.Decimal, int,  | decimal.Decimal,  | How often this alarm is triggered | 
**subtype** | [**DataSubtype**](DataSubtype.md) | [**DataSubtype**](DataSubtype.md) |  | 
**assetId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the corresponding asset | 
**priority** | [**AlarmPriority**](AlarmPriority.md) | [**AlarmPriority**](AlarmPriority.md) |  | 
**timestamp** | str, datetime,  | str,  | Timestamp of the latest data change | value must conform to RFC-3339 date-time
**ruleId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of the corresponding rule | [optional] 
**attribute** | None, str,  | NoneClass, str,  | Name of the attribute of the asset type | [optional] 
**requiresAcknowledge** | bool,  | BoolClass,  | Requires the alarm an acknowledgment | [optional] if omitted the server will use the default value of False
**value** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The value which triggers the alarm | [optional] value must be a 64 bit float
**goneTimestamp** | None, str, datetime,  | NoneClass, str,  | Timestamp of the latest data change | [optional] value must conform to RFC-3339 date-time
**acknowledgeTimestamp** | None, str, datetime,  | NoneClass, str,  | Timestamp of the latest data change | [optional] value must conform to RFC-3339 date-time
**acknowledgeText** | None, str,  | NoneClass, str,  | Text of acknowledgement | [optional] 
**acknowledgeUserId** | None, str,  | NoneClass, str,  | User who acknowledged the alarm | [optional] 
**[message](#message)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Message texts for alarm | [optional] 
**assetInfo** | [**Asset**](Asset.md) | [**Asset**](Asset.md) |  | [optional] 
**ruleInfo** | [**AlarmRule**](AlarmRule.md) | [**AlarmRule**](AlarmRule.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# message

Message texts for alarm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Message texts for alarm | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


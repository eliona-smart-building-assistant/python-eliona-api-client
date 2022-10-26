# eliona.api_client.model.alarm_rule.AlarmRule

Rule for an alarm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Rule for an alarm | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**subtype** | [**DataSubtype**](DataSubtype.md) | [**DataSubtype**](DataSubtype.md) |  | 
**assetId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the corresponding asset | 
**attribute** | str,  | str,  | Name of the attribute of the asset type | 
**priority** | [**AlarmPriority**](AlarmPriority.md) | [**AlarmPriority**](AlarmPriority.md) |  | 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of the rule | [optional] 
**enable** | bool,  | BoolClass,  | Rule enabled or not | [optional] if omitted the server will use the default value of True
**requiresAcknowledge** | bool,  | BoolClass,  | Requires the alarm an acknowledgment | [optional] if omitted the server will use the default value of False
**equal** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Triggers alarm if attribute value equals this value | [optional] value must be a 64 bit float
**low** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Triggers alarm if attribute value is less than value | [optional] value must be a 64 bit float
**high** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Triggers alarm if attribute value is greater than value | [optional] value must be a 64 bit float
**[message](#message)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Message texts for alarm | [optional] 
**[tags](#tags)** | list, tuple, None,  | tuple, NoneClass,  | List of associated tags | [optional] 
**subject** | None, str,  | NoneClass, str,  | The subject for the alarm | [optional] 
**urldoc** | None, str,  | NoneClass, str,  | The url describing the alarm | [optional] 
**notifyOn** | None, str,  | NoneClass, str,  | Notification | [optional] 
**dontMask** | None, bool,  | NoneClass, BoolClass,  | Do not mask | [optional] if omitted the server will use the default value of False
**assetInfo** | [**Asset**](Asset.md) | [**Asset**](Asset.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# message

Message texts for alarm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Message texts for alarm | 

# tags

List of associated tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of associated tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


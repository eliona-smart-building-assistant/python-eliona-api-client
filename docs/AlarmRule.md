# AlarmRule

Rule for an alarm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**attribute** | **str** | Name of the attribute of the asset type | 
**priority** | [**AlarmPriority**](AlarmPriority.md) |  | 
**id** | **int, none_type** | The id of the rule | [optional] [readonly] 
**enable** | **bool** | Rule enabled or not | [optional]  if omitted the server will use the default value of True
**requires_acknowledge** | **bool** | Requires the alarm an acknowledgment | [optional]  if omitted the server will use the default value of False
**equal** | **float, none_type** | Triggers alarm if attribute value equals this value | [optional] 
**low** | **float, none_type** | Triggers alarm if attribute value is less than value | [optional] 
**high** | **float, none_type** | Triggers alarm if attribute value is greater than value | [optional] 
**message** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Texts for alarm | [optional] 
**tags** | **[str], none_type** | List of associated tags | [optional] 
**subject** | **str, none_type** | The subject for the alarm | [optional] 
**urldoc** | **str, none_type** | The url describing the alarm | [optional] 
**params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Parameter for aggregated alarms | [optional] 
**notify_on** | **str, none_type** | Notification | [optional] 
**dont_mask** | **bool, none_type** | Do not mask | [optional]  if omitted the server will use the default value of False
**check_type** | **str, none_type** | Check type | [optional] 
**asset_info** | [**Asset**](Asset.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



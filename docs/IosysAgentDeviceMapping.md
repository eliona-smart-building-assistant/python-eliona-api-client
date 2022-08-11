# IosysAgentDeviceMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype** | [**HeapSubtype**](HeapSubtype.md) |  | 
**attribute** | **str** | Name of the attribute to map | 
**_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | **int, none_type** | Unique id for the mapping | [optional] [readonly] 
**device_id** | **int, none_type** | The id of the device the mapping belongs to | [optional] [readonly] 
**enable** | **bool** | Is the mapping enabled or not | [optional]  if omitted the server will use the default value of True
**asset_id** | **int, none_type** | ID of the corresponding asset | [optional] 
**ios_var** | **str, none_type** |  | [optional] 
**ios_type** | **str, none_type** |  | [optional] 
**down** | **bool, none_type** |  | [optional]  if omitted the server will use the default value of False
**scale** | **float, none_type** |  | [optional] 
**zero** | **float, none_type** |  | [optional] 
**mask** | **[int], none_type** |  | [optional] 
**mask_attributes** | **[str], none_type** |  | [optional] 
**dead_time** | **int, none_type** |  | [optional] 
**dead_band** | **float, none_type** |  | [optional] 
**filter** | **str, none_type** |  | [optional] 
**tau** | **float, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



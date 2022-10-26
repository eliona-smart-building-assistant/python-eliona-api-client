# eliona.api_client.model.agent_device_mapping_general.AgentDeviceMappingGeneral

A general mapping of attributes for an agent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A general mapping of attributes for an agent | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**subtype** | [**DataSubtype**](DataSubtype.md) | [**DataSubtype**](DataSubtype.md) |  | 
**attribute** | str,  | str,  | Name of the attribute to map | 
**class** | [**AgentClass**](AgentClass.md) | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Unique id for the mapping | [optional] 
**deviceId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of the device the mapping belongs to | [optional] 
**enable** | bool,  | BoolClass,  | Is the mapping enabled or not | [optional] if omitted the server will use the default value of True
**assetId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | ID of the corresponding asset | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


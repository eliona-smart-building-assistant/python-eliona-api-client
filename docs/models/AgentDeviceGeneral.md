# eliona.api_client.model.agent_device_general.AgentDeviceGeneral

A general device for an agent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A general device for an agent | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**class** | [**AgentClass**](AgentClass.md) | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Unique id for the device | [optional] 
**agentId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of the agent the device belongs to | [optional] 
**enable** | bool,  | BoolClass,  | Is the device enabled or not | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


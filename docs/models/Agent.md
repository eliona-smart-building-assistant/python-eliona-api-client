# eliona.api_client.model.agent.Agent

An agent installed on an edge node

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | An agent installed on an edge node | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Unique id for the agent | [optional] 
**nodeId** | None, str,  | NoneClass, str,  | Id of the node where the agent is installed | [optional] 
**assetId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | ID of the corresponding asset | [optional] 
**class** | [**AgentClass**](AgentClass.md) | [**AgentClass**](AgentClass.md) |  | [optional] 
**description** | None, str,  | NoneClass, str,  | Descriptive text for the agent | [optional] 
**enable** | bool,  | BoolClass,  | Is the agent enabled or not | [optional] if omitted the server will use the default value of False
**[config](#config)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Individual configuration depending on agent class | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# config

Individual configuration depending on agent class

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Individual configuration depending on agent class | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


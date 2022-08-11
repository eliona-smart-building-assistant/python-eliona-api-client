# Agent

An agent installed on an edge node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Unique id for the agent | [optional] [readonly] 
**node_id** | **str, none_type** | Id of the node where the agent is installed | [optional] 
**asset_id** | **int, none_type** | ID of the corresponding asset | [optional] 
**_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**description** | **str, none_type** | Descriptive text for the agent | [optional] 
**enable** | **bool** | Is the agent enabled or not | [optional]  if omitted the server will use the default value of False
**config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Individual configuration depending on agent class | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



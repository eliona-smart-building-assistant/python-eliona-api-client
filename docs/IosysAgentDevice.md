# IosysAgentDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | **int, none_type** | Unique id for the device | [optional] [readonly] 
**agent_id** | **int, none_type** | The id of the agent the device belongs to | [optional] [readonly] 
**enable** | **bool** | Is the device enabled or not | [optional]  if omitted the server will use the default value of False
**port** | **int, none_type** | Port of device | [optional] 
**certificate** | **str, none_type** | Certificate of device | [optional] 
**key** | **str, none_type** | Key for device | [optional] 
**timeout** | **int, none_type** | Time in seconds | [optional] 
**reconnect** | **int, none_type** | Reconnect | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



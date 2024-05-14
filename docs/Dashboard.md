# Dashboard

A frontend dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for this dashboard | 
**project_id** | **str** | ID of the project to which the dashboard belongs | 
**user_id** | **str** | ID of the user who owns the dashboard | 
**id** | **int, none_type** | The internal Id of dashboard | [optional] [readonly] 
**sequence** | **int, none_type** | The sequence of the dashboard | [optional]  if omitted the server will use the default value of 0
**widgets** | [**[Widget], none_type**](Widget.md) | List of widgets on this dashboard (order matches the order of widgets on the dashboard) | [optional] 
**public** | **bool, none_type** | Is the dashboard public and not bound to a dedicated user | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



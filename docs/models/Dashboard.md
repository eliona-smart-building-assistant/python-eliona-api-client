# eliona.api_client.model.dashboard.Dashboard

A frontend dashboard

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A frontend dashboard | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name for this dashboard | 
**projectId** | str,  | str,  | ID of the project to which the dashboard belongs | 
**userId** | str,  | str,  | ID of the user who owns the dashboard | 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The internal Id of dashboard | [optional] 
**sequence** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The sequence of the dashboard | [optional] if omitted the server will use the default value of 0
**[widgets](#widgets)** | list, tuple, None,  | tuple, NoneClass,  | List of widgets on this dashboard (order matches the order of widgets on the dashboard) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# widgets

List of widgets on this dashboard (order matches the order of widgets on the dashboard)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of widgets on this dashboard (order matches the order of widgets on the dashboard) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Widget**](Widget.md) | [**Widget**](Widget.md) | [**Widget**](Widget.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


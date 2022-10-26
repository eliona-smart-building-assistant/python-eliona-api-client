# eliona.api_client.model.widget_data.WidgetData

Data for a widget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data for a widget | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The internal Id of widget data | [optional] 
**elementSequence** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Position of the element in widget type | [optional] 
**assetId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The master asset id of this widget | [optional] 
**[data](#data)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | individual config parameters depending on category | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

individual config parameters depending on category

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | individual config parameters depending on category | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


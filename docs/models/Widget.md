# eliona.api_client.model.widget.Widget

A widget on a frontend dashboard

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A widget on a frontend dashboard | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**width** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**widgetTypeName** | str,  | str,  | The name for the type of this widget | 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The internal Id of widget | [optional] 
**[details](#details)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Detailed configuration depending on the widget type | [optional] 
**assetId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The master asset id of this widget | [optional] 
**sequence** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Placement order on dashboard; if not set the index in array is taken | [optional] 
**[data](#data)** | list, tuple, None,  | tuple, NoneClass,  | List of data for the elements of widget | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# details

Detailed configuration depending on the widget type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Detailed configuration depending on the widget type | 

# data

List of data for the elements of widget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of data for the elements of widget | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WidgetData**](WidgetData.md) | [**WidgetData**](WidgetData.md) | [**WidgetData**](WidgetData.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


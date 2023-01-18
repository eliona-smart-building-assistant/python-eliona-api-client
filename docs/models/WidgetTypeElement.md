# eliona.api_client.model.widget_type_element.WidgetTypeElement

An element for widget types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An element for widget types | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**category** | str,  | str,  | The category for this element | must be one of ["input", "table", "image", "tickets", "map", "icon", "range", "donut", "comfort", "sankey", "progress", "tracking", "heatmap", "radar", "value", "calendar", "trend", "alarms", "weather", "storey", ] 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The internal Id of widget element | [optional] 
**sequence** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | sequence of element in widget; if not defined the index in array is taken | [optional] 
**[config](#config)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | individual config parameters depending on category | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# config

individual config parameters depending on category

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | individual config parameters depending on category | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


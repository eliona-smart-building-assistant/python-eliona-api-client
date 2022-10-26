# eliona.api_client.model.widget_type.WidgetType

A frontend widget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A frontend widget | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[elements](#elements)** | list, tuple,  | tuple,  | A list of elements for this widget (order matches the order of elements for this type) | 
**name** | str,  | str,  | The unique name for this widget type | 
**translation** | [**Translation**](Translation.md) | [**Translation**](Translation.md) |  | 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The internal Id of widget type | [optional] 
**custom** | bool,  | BoolClass,  | Is this a customer created type or not | [optional] if omitted the server will use the default value of True
**icon** | None, str,  | NoneClass, str,  | Icon name corresponding to assets used in this widget | [optional] 
**withAlarm** | None, bool,  | NoneClass, BoolClass,  | Show alarms in widget | [optional] if omitted the server will use the default value of False
**withTimespan** | None, bool,  | NoneClass, BoolClass,  | Show selection for timespan in widget | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# elements

A list of elements for this widget (order matches the order of elements for this type)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of elements for this widget (order matches the order of elements for this type) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WidgetTypeElement**](WidgetTypeElement.md) | [**WidgetTypeElement**](WidgetTypeElement.md) | [**WidgetTypeElement**](WidgetTypeElement.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


# WidgetType

A frontend widget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this widget type | 
**translation** | [**Translation**](Translation.md) |  | 
**elements** | [**[WidgetTypeElement]**](WidgetTypeElement.md) | A list of elements for this widget (order matches the order of elements for this type) | 
**id** | **int, none_type** | The internal Id of widget type | [optional] [readonly] 
**custom** | **bool** | Is this a customer created type or not | [optional]  if omitted the server will use the default value of True
**icon** | **str, none_type** | Icon name corresponding to assets used in this widget | [optional] 
**with_alarm** | **bool, none_type** | Show alarms in widget | [optional]  if omitted the server will use the default value of False
**with_timespan** | **bool, none_type** | Show selection for timespan in widget | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



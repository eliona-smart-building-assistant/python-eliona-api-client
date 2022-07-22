# Widget

A widget on a frontend dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widget_type_name** | **str** | The name for the type of this widget | 
**width** | **str** | The width of this widget on dashboard | 
**timespan** | **int, none_type** | The number of days if the widget type uses timespan | [optional] 
**details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Detailed configuration depending on the widget type | [optional] 
**asset_id** | **int, none_type** | The master asset id of this widget | [optional] 
**data** | [**[WidgetData], none_type**](WidgetData.md) | List of data for the elements of widget | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



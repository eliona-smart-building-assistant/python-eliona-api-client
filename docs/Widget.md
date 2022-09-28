# Widget

A widget on a frontend dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widget_type_name** | **str** | The name for the type of this widget | 
**id** | **int, none_type** | The internal Id of widget | [optional] [readonly] 
**details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Detailed configuration depending on the widget type | [optional] 
**asset_id** | **int, none_type** | The master asset id of this widget | [optional] 
**sequence** | **int, none_type** | Placement order on dashboard; if not set the index in array is taken | [optional] 
**data** | [**[WidgetData], none_type**](WidgetData.md) | List of data for the elements of widget | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



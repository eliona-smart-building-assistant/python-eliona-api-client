# DataAggregated

Aggregated data combines multiple data points for a periodical raster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**raster** | **str** | Calculation intervals. | 
**aggregation_id** | **int** | ID of the aggregation | [optional] 
**attribute** | **str** | Name of the attribute which holds the data points | [optional] 
**timestamp** | **datetime, none_type** | Timestamp of this aggregated data set | [optional] 
**count** | **float, none_type** | Count of data points in this aggregated data set | [optional] 
**average** | **float, none_type** | Average of all data points for this aggregated data set | [optional] 
**sum** | **float, none_type** | Sum of all data points for this aggregated data set | [optional] 
**first** | **float, none_type** | First data point in this aggregated data set | [optional] 
**min** | **float, none_type** | Data point with the most minimal value in this aggregated data set | [optional] 
**max** | **float, none_type** | Data point with the most maximal value in this aggregated data set | [optional] 
**last** | **float, none_type** | Latest data point in this aggregated data set | [optional] 
**last_timestamp** | **datetime, none_type** | Timestamp of the latest data point | [optional] 
**asset_type_name** | **str, none_type** | The name of the corresponding asset type | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



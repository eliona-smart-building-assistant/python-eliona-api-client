# Data

Data for assets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Asset payload | 
**timestamp** | **datetime, none_type** | Timestamp of the latest data change | [optional] 
**asset_type_name** | **str, none_type** | The name of the corresponding asset type | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



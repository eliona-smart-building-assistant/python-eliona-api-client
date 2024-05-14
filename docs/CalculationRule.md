# CalculationRule

Calculation rule to calculate asset attribute data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**attribute** | **str** | Name of the attribute of the asset type to be calculated | 
**id** | **int, none_type** | The id of the rule | [optional] [readonly] 
**virtual** | **bool, none_type** | Is the calculation attribute virtual or not | [optional] 
**formula** | **str, none_type** | calculation rule to calculate the value for the attribute | [optional] 
**unit** | **str, none_type** | Physical unit of calculated data | [optional] 
**filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Filter definition for calculation rule | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



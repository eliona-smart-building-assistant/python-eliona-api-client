# AttributeDisplay

How attributes are displayed for specific assets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**attribute** | **str** | Name of the attribute of the asset type | 
**unit** | **str, none_type** | Physical unit of numeric data | [optional] 
**precision** | **int, none_type** | Number of decimal places | [optional] 
**min** | **float, none_type** | Lower limit | [optional] 
**max** | **float, none_type** | Upper limit | [optional] 
**viewer** | **bool, none_type** | Should the attribute be displayed in viewer | [optional]  if omitted the server will use the default value of False
**ar** | **bool, none_type** | Should the attribute be displayed in AR | [optional]  if omitted the server will use the default value of False
**sequence** | **int, none_type** | Sequence in AR display | [optional] 
**map** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type** | list of mapping between value and custom text | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



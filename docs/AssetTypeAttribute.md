# AssetTypeAttribute

Named attribute to store data of assets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique key of asset data | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**asset_type_name** | **str, none_type** | The unique name for the asset type | [optional] 
**type** | **str, none_type** | Name of the type for this attribute | [optional] 
**enable** | **bool** | Is data active or not | [optional]  if omitted the server will use the default value of True
**translation** | [**Translation**](Translation.md) |  | [optional] 
**unit** | **str, none_type** | Physical unit of numeric data | [optional] 
**precision** | **int, none_type** | Number of decimal places | [optional] 
**min** | **float, none_type** | Lower limit | [optional] 
**max** | **float, none_type** | Upper limit | [optional] 
**pipeline** | [**Pipeline**](Pipeline.md) |  | [optional] 
**viewer** | **bool, none_type** | Should the attribute be displayed in viewer | [optional]  if omitted the server will use the default value of False
**ar** | **bool, none_type** | Should the attribute be displayed in AR | [optional]  if omitted the server will use the default value of False
**sequence** | **int, none_type** | Sequence in AR display | [optional] 
**virtual** | **bool, none_type** | Is the attribute virtual or not | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



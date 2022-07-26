# eliona.api_client.model.asset_type.AssetType

A type of assets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A type of assets | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The unique name for this asset type | 
**custom** | bool,  | BoolClass,  | Is this a customer created type or not | [optional] if omitted the server will use the default value of True
**vendor** | None, str,  | NoneClass, str,  | The vendor providing assets of this type | [optional] 
**model** | None, str,  | NoneClass, str,  | The specific model of assets of this type | [optional] 
**translation** | [**Translation**](Translation.md) | [**Translation**](Translation.md) |  | [optional] 
**urldoc** | None, str,  | NoneClass, str,  | The url describing assets of this type | [optional] 
**icon** | None, str,  | NoneClass, str,  | Icon name corresponding to assets of this type | [optional] 
**payloadFunction** | None, str,  | NoneClass, str,  | Asset types payload function | [optional] 
**allowedInactivity** | None, str,  | NoneClass, str,  |  | [optional] 
**[attributes](#attributes)** | list, tuple, None,  | tuple, NoneClass,  | List of named attributes | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributes

List of named attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of named attributes | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AssetTypeAttribute**](AssetTypeAttribute.md) | [**AssetTypeAttribute**](AssetTypeAttribute.md) | [**AssetTypeAttribute**](AssetTypeAttribute.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


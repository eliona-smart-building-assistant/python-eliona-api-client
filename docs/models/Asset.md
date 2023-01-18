# eliona.api_client.model.asset.Asset

An asset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | An asset | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**globalAssetIdentifier** | str,  | str,  | Unique identifier for the asset | 
**projectId** | str,  | str,  | ID of the project to which the asset belongs | 
**assetType** | str,  | str,  | Reference to asset type by name | 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The internal Id of asset | [optional] 
**name** | None, str,  | NoneClass, str,  | Alternate text for the asset to display in frontend | [optional] 
**latitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Latitude coordinate (GPS) of the asset | [optional] value must be a 64 bit float
**longitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Longitude coordinate (GPS) of the asset | [optional] value must be a 64 bit float
**description** | None, str,  | NoneClass, str,  | Textual description for this asset | [optional] 
**parentFunctionalAssetId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of an asset which groups this asset as a functional child | [optional] 
**parentLocationalAssetId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of an asset which groups this asset as a locational child | [optional] 
**[tags](#tags)** | list, tuple, None,  | tuple, NoneClass,  | List of associated tags | [optional] 
**[childrenInfo](#childrenInfo)** | list, tuple, None,  | tuple, NoneClass,  | List of children for this asset. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

List of associated tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of associated tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# childrenInfo

List of children for this asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of children for this asset. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Asset**](Asset.md) | [**Asset**](Asset.md) | [**Asset**](Asset.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


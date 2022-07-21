# AssetType

A type of assets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this asset type | 
**custom** | **bool** | Is this a customer created type or not | defaults to True
**vendor** | **str** | The vendor providing assets of this type | [optional] 
**model** | **str** | The specific model of assets of this type | [optional] 
**translation** | [**Translation**](Translation.md) |  | [optional] 
**urldoc** | **str** | The url describing assets of this type | [optional] 
**icon** | **str** | Icon name corresponding to assets of this type | [optional] 
**attributes** | [**[AssetTypeAttribute]**](AssetTypeAttribute.md) | List of named attributes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



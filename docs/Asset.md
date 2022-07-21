# Asset

An asset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project to which the asset belongs | 
**global_asset_identifier** | **str** | Unique identifier for the asset | 
**asset_type** | **str** | Reference to asset type by name | 
**id** | **int** | The internal Id of asset | [optional] [readonly] 
**name** | **str** | Alternate text for the asset to display in frontend | [optional] 
**latitude** | **float** | Latitude coordinate (GPS) of the asset | [optional] 
**longitude** | **float** | Longitude coordinate (GPS) of the asset | [optional] 
**description** | **str** | Textual description for this asset | [optional] 
**parent_functional_asset_id** | **int** | The id of an asset which groups this asset as a functional child | [optional] 
**parent_locational_asset_id** | **int** | The id of an asset which groups this asset as a locational child | [optional] 
**tags** | **[str]** | List of tags associated with asset | [optional] 
**children** | [**[Asset]**](Asset.md) | List of children for this asset. This list is filled when the &#x60;withChildren&#x60; parameter is set. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



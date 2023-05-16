# Asset

An asset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project to which the asset belongs | 
**global_asset_identifier** | **str** | Unique identifier for the asset | 
**asset_type** | **str** | Reference to asset type by name | 
**id** | **int, none_type** | The internal Id of asset | [optional] [readonly] 
**name** | **str, none_type** | Alternate text for the asset to display in frontend | [optional] 
**latitude** | **float, none_type** | Latitude coordinate (GPS) of the asset | [optional] 
**longitude** | **float, none_type** | Longitude coordinate (GPS) of the asset | [optional] 
**is_tracker** | **bool, none_type** | Does the asset function as a tracker and capture its position by itself | [optional]  if omitted the server will use the default value of False
**description** | **str, none_type** | Textual description for this asset | [optional] 
**parent_functional_asset_id** | **int, none_type** | The id of an asset which groups this asset as a functional child | [optional] 
**parent_locational_asset_id** | **int, none_type** | The id of an asset which groups this asset as a locational child | [optional] 
**tags** | **[str], none_type** | List of associated tags | [optional] 
**children_info** | [**[Asset], none_type**](Asset.md) | List of children for this asset. | [optional] [readonly] 
**attachments** | [**[Attachment], none_type**](Attachment.md) | A list of files attached to the asset | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



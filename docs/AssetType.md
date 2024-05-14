# AssetType

A type of assets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this asset type | 
**custom** | **bool** | Is this a customer created type or not | [optional]  if omitted the server will use the default value of True
**vendor** | **str, none_type** | The vendor providing assets of this type | [optional] 
**model** | **str, none_type** | The specific model of assets of this type | [optional] 
**translation** | [**Translation**](Translation.md) |  | [optional] 
**urldoc** | **str, none_type** | The url describing assets of this type | [optional] 
**icon** | **str, none_type** | Icon name corresponding to assets of this type: blind, building, button, closable, elevator, environment, fallback, filling, gateway, light, mailbox, parking, people, power, rack, storey, trash, ventilation, vibration, water, weather | [optional] 
**payload_function** | **str, none_type** | Asset types payload function | [optional] 
**allowed_inactivity** | **str, none_type** |  | [optional] 
**is_tracker** | **bool, none_type** | Function as a tracker | [optional]  if omitted the server will use the default value of False
**attributes** | [**[AssetTypeAttribute], none_type**](AssetTypeAttribute.md) | List of named attributes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DataListen


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Asset payload | 
**status_code** | **int** | The status code expecting when actually perform the operation. Some values are - 200: updated (ok)  - 201: created - 204: deleted (no content) - 304: unchanged (not modified) - 400: problem (bad request) - 404: not found - 409: duplicated (conflict) - 422: unprocessable  | [optional] 
**timestamp** | **datetime, none_type** | Timestamp of the latest data change | [optional] 
**asset_type_name** | **str, none_type** | The name of the corresponding asset type | [optional] [readonly] 
**client_reference** | **str, none_type** | freely assignable by the client to identify self-created data | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



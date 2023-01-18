# eliona.api_client.model.node.Node

An edge node

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | An edge node | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | None, str,  | NoneClass, str,  | Unique id for the edge node | [optional] 
**ident** | None, str,  | NoneClass, str,  | UUID to identify the edge node | [optional] 
**password** | None, str,  | NoneClass, str,  | Password with which the node identifies itself | [optional] 
**assetId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | ID of the corresponding asset | [optional] 
**vendor** | None, str,  | NoneClass, str,  | Vendor name | [optional] 
**model** | None, str,  | NoneClass, str,  | Model name | [optional] 
**description** | None, str,  | NoneClass, str,  | Descriptive text for the edge node | [optional] 
**enable** | bool,  | BoolClass,  | Is the node enabled or not | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


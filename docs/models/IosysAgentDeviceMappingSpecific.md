# eliona.api_client.model.iosys_agent_device_mapping_specific.IosysAgentDeviceMappingSpecific

Specific mapping for IOSYS agents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Specific mapping for IOSYS agents | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**iosVar** | None, str,  | NoneClass, str,  |  | [optional] 
**iosType** | None, str,  | NoneClass, str,  |  | [optional] must be one of ["INT", "REAL", "STRING", ] 
**down** | None, bool,  | NoneClass, BoolClass,  |  | [optional] if omitted the server will use the default value of False
**scale** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**zero** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**[mask](#mask)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[maskAttributes](#maskAttributes)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**deadTime** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**deadBand** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**filter** | None, str,  | NoneClass, str,  |  | [optional] must be one of ["LPF1", "LPF2", "MOVA", ] 
**tau** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mask

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# maskAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


# eliona.api_client.model.asset_type_attribute.AssetTypeAttribute

Named attribute to store data of assets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Named attribute to store data of assets | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**subtype** | [**DataSubtype**](DataSubtype.md) | [**DataSubtype**](DataSubtype.md) |  | 
**name** | str,  | str,  | Unique key of asset data | 
**assetTypeName** | None, str,  | NoneClass, str,  | The unique name for the asset type | [optional] 
**type** | None, str,  | NoneClass, str,  | Name of the type for this attribute | [optional] must be one of ["battery-voltage", "brightness", "co2", "current", "device-info", "device-status", "energy", "flow", "frequency", "humidity", "inputs-and-switches", "level", "motion", "operating-status", "people-count", "power", "presence", "pressure", "temperature", "vehicle-detector", "voltage", "watchdog", "weather", "voc", ] 
**enable** | bool,  | BoolClass,  | Is data active or not | [optional] if omitted the server will use the default value of True
**translation** | [**Translation**](Translation.md) | [**Translation**](Translation.md) |  | [optional] 
**unit** | None, str,  | NoneClass, str,  | Physical unit of numeric data | [optional] 
**precision** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Number of decimal places | [optional] value must be a 64 bit integer
**min** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Lower limit | [optional] value must be a 64 bit float
**max** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Upper limit | [optional] value must be a 64 bit float
**aggregationMode** | None, str,  | NoneClass, str,  | Aggregation calculation mode | [optional] must be one of ["avg", "sum", "cusum", ] 
**[aggregationRasters](#aggregationRasters)** | list, tuple,  | tuple,  |  | [optional] 
**viewer** | None, bool,  | NoneClass, BoolClass,  | Should the attribute be displayed in viewer | [optional] if omitted the server will use the default value of False
**ar** | None, bool,  | NoneClass, BoolClass,  | Should the attribute be displayed in AR | [optional] if omitted the server will use the default value of False
**sequence** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Sequence in AR display | [optional] value must be a 64 bit integer
**virtual** | None, bool,  | NoneClass, BoolClass,  | Is the attribute virtual or not | [optional] 
**scale** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | value scale | [optional] 
**zero** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | value scale | [optional] 
**[map](#map)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | custom map | [optional] 
**[sourcePath](#sourcePath)** | list, tuple, None,  | tuple, NoneClass,  | source path for attribute value | [optional] 
**isDigital** | None, bool,  | NoneClass, BoolClass,  | is attribute digital | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# aggregationRasters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Aggregation calculation intervals | must be one of ["S1", "S2", "S3", "S4", "S5", "S6", "S10", "S12", "S15", "S20", "S30", "M1", "M2", "M3", "M4", "M5", "M6", "M10", "M12", "M15", "M20", "M30", "H1", "H2", "H3", "H4", "H6", "H8", "H12", "DAY", "WEEK", "MONTH", "QUARTER", "YEAR", "DECADE", "CENTURY", ] 

# map

custom map

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | custom map | 

# sourcePath

source path for attribute value

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | source path for attribute value | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


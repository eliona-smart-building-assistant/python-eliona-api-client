# eliona.api_client.model.aggregation.Aggregation

Defines the aggregation of data points

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Defines the aggregation of data points | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mode** | str,  | str,  | Calculation mode | must be one of ["avg", "sum", "cusum", ] 
**subtype** | [**DataSubtype**](DataSubtype.md) | [**DataSubtype**](DataSubtype.md) |  | 
**assetId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the corresponding asset | 
**id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | ID of the aggregation | [optional] 
**attribute** | str,  | str,  | Name of the attribute which holds the data points | [optional] 
**raster** | None, str,  | NoneClass, str,  | calculation interval | [optional] must be one of ["S1", "S2", "S3", "S4", "S5", "S6", "S10", "S12", "S15", "S20", "S30", "M1", "M2", "M3", "M4", "M5", "M6", "M10", "M12", "M15", "M20", "M30", "H1", "H2", "H3", "H4", "H6", "H8", "H12", "DAY", "WEEK", "MONTH", "QUARTER", "YEAR", "DECADE", "CENTURY", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


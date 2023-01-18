# eliona.api_client.model.data_aggregated.DataAggregated

Aggregated data combines multiple data points for a periodical raster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Aggregated data combines multiple data points for a periodical raster | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**subtype** | [**DataSubtype**](DataSubtype.md) | [**DataSubtype**](DataSubtype.md) |  | 
**assetId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the corresponding asset | 
**raster** | str,  | str,  | Calculation intervals. | must be one of ["S1", "S2", "S3", "S4", "S5", "S6", "S10", "S12", "S15", "S20", "S30", "M1", "M2", "M3", "M4", "M5", "M6", "M10", "M12", "M15", "M20", "M30", "H1", "H2", "H3", "H4", "H6", "H8", "H12", "DAY", "WEEK", "MONTH", "QUARTER", "YEAR", "DECADE", "CENTURY", ] 
**id** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**aggregationId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the aggregation | [optional] 
**attribute** | str,  | str,  | Name of the attribute which holds the data points | [optional] 
**timestamp** | None, str, datetime,  | NoneClass, str,  | Timestamp of this aggregated data set | [optional] value must conform to RFC-3339 date-time
**count** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Count of data points in this aggregated data set | [optional] value must be a 64 bit float
**average** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Average of all data points for this aggregated data set | [optional] value must be a 64 bit float
**sum** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Sum of all data points for this aggregated data set | [optional] value must be a 64 bit float
**first** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | First data point in this aggregated data set | [optional] value must be a 64 bit float
**min** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Data point with the most minimal value in this aggregated data set | [optional] value must be a 64 bit float
**max** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Data point with the most maximal value in this aggregated data set | [optional] value must be a 64 bit float
**last** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Latest data point in this aggregated data set | [optional] value must be a 64 bit float
**lastTimestamp** | None, str, datetime,  | NoneClass, str,  | Timestamp of the latest data point | [optional] value must conform to RFC-3339 date-time
**assetTypeName** | None, str,  | NoneClass, str,  | The name of the corresponding asset type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


# coding: utf-8

"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.4.2
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from eliona.api_client import schemas  # noqa: F401


class AssetTypeAttribute(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Named attribute to store data of assets
    """


    class MetaOapg:
        required = {
            "subtype",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def subtype() -> typing.Type['DataSubtype']:
                return DataSubtype
            
            
            class assetTypeName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assetTypeName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class type(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "battery-voltage": "BATTERYVOLTAGE",
                        "brightness": "BRIGHTNESS",
                        "co2": "CO2",
                        "current": "CURRENT",
                        "device-info": "DEVICEINFO",
                        "device-status": "DEVICESTATUS",
                        "energy": "ENERGY",
                        "flow": "FLOW",
                        "frequency": "FREQUENCY",
                        "humidity": "HUMIDITY",
                        "inputs-and-switches": "INPUTSANDSWITCHES",
                        "level": "LEVEL",
                        "motion": "MOTION",
                        "operating-status": "OPERATINGSTATUS",
                        "people-count": "PEOPLECOUNT",
                        "power": "POWER",
                        "presence": "PRESENCE",
                        "pressure": "PRESSURE",
                        "temperature": "TEMPERATURE",
                        "vehicle-detector": "VEHICLEDETECTOR",
                        "voltage": "VOLTAGE",
                        "watchdog": "WATCHDOG",
                        "weather": "WEATHER",
                        "voc": "VOC",
                    }
                
                @schemas.classproperty
                def BATTERYVOLTAGE(cls):
                    return cls("battery-voltage")
                
                @schemas.classproperty
                def BRIGHTNESS(cls):
                    return cls("brightness")
                
                @schemas.classproperty
                def CO2(cls):
                    return cls("co2")
                
                @schemas.classproperty
                def CURRENT(cls):
                    return cls("current")
                
                @schemas.classproperty
                def DEVICEINFO(cls):
                    return cls("device-info")
                
                @schemas.classproperty
                def DEVICESTATUS(cls):
                    return cls("device-status")
                
                @schemas.classproperty
                def ENERGY(cls):
                    return cls("energy")
                
                @schemas.classproperty
                def FLOW(cls):
                    return cls("flow")
                
                @schemas.classproperty
                def FREQUENCY(cls):
                    return cls("frequency")
                
                @schemas.classproperty
                def HUMIDITY(cls):
                    return cls("humidity")
                
                @schemas.classproperty
                def INPUTSANDSWITCHES(cls):
                    return cls("inputs-and-switches")
                
                @schemas.classproperty
                def LEVEL(cls):
                    return cls("level")
                
                @schemas.classproperty
                def MOTION(cls):
                    return cls("motion")
                
                @schemas.classproperty
                def OPERATINGSTATUS(cls):
                    return cls("operating-status")
                
                @schemas.classproperty
                def PEOPLECOUNT(cls):
                    return cls("people-count")
                
                @schemas.classproperty
                def POWER(cls):
                    return cls("power")
                
                @schemas.classproperty
                def PRESENCE(cls):
                    return cls("presence")
                
                @schemas.classproperty
                def PRESSURE(cls):
                    return cls("pressure")
                
                @schemas.classproperty
                def TEMPERATURE(cls):
                    return cls("temperature")
                
                @schemas.classproperty
                def VEHICLEDETECTOR(cls):
                    return cls("vehicle-detector")
                
                @schemas.classproperty
                def VOLTAGE(cls):
                    return cls("voltage")
                
                @schemas.classproperty
                def WATCHDOG(cls):
                    return cls("watchdog")
                
                @schemas.classproperty
                def WEATHER(cls):
                    return cls("weather")
                
                @schemas.classproperty
                def VOC(cls):
                    return cls("voc")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            enable = schemas.BoolSchema
        
            @staticmethod
            def translation() -> typing.Type['Translation']:
                return Translation
            
            
            class unit(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unit':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class precision(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'precision':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class min(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'min':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class max(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'max':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class aggregationMode(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "avg": "AVG",
                        "sum": "SUM",
                        "cusum": "CUSUM",
                    }
                
                @schemas.classproperty
                def AVG(cls):
                    return cls("avg")
                
                @schemas.classproperty
                def SUM(cls):
                    return cls("sum")
                
                @schemas.classproperty
                def CUSUM(cls):
                    return cls("cusum")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'aggregationMode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class aggregationRasters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def S1(cls):
                            return cls("S1")
                        
                        @schemas.classproperty
                        def S2(cls):
                            return cls("S2")
                        
                        @schemas.classproperty
                        def S3(cls):
                            return cls("S3")
                        
                        @schemas.classproperty
                        def S4(cls):
                            return cls("S4")
                        
                        @schemas.classproperty
                        def S5(cls):
                            return cls("S5")
                        
                        @schemas.classproperty
                        def S6(cls):
                            return cls("S6")
                        
                        @schemas.classproperty
                        def S10(cls):
                            return cls("S10")
                        
                        @schemas.classproperty
                        def S12(cls):
                            return cls("S12")
                        
                        @schemas.classproperty
                        def S15(cls):
                            return cls("S15")
                        
                        @schemas.classproperty
                        def S20(cls):
                            return cls("S20")
                        
                        @schemas.classproperty
                        def S30(cls):
                            return cls("S30")
                        
                        @schemas.classproperty
                        def M1(cls):
                            return cls("M1")
                        
                        @schemas.classproperty
                        def M2(cls):
                            return cls("M2")
                        
                        @schemas.classproperty
                        def M3(cls):
                            return cls("M3")
                        
                        @schemas.classproperty
                        def M4(cls):
                            return cls("M4")
                        
                        @schemas.classproperty
                        def M5(cls):
                            return cls("M5")
                        
                        @schemas.classproperty
                        def M6(cls):
                            return cls("M6")
                        
                        @schemas.classproperty
                        def M10(cls):
                            return cls("M10")
                        
                        @schemas.classproperty
                        def M12(cls):
                            return cls("M12")
                        
                        @schemas.classproperty
                        def M15(cls):
                            return cls("M15")
                        
                        @schemas.classproperty
                        def M20(cls):
                            return cls("M20")
                        
                        @schemas.classproperty
                        def M30(cls):
                            return cls("M30")
                        
                        @schemas.classproperty
                        def H1(cls):
                            return cls("H1")
                        
                        @schemas.classproperty
                        def H2(cls):
                            return cls("H2")
                        
                        @schemas.classproperty
                        def H3(cls):
                            return cls("H3")
                        
                        @schemas.classproperty
                        def H4(cls):
                            return cls("H4")
                        
                        @schemas.classproperty
                        def H6(cls):
                            return cls("H6")
                        
                        @schemas.classproperty
                        def H8(cls):
                            return cls("H8")
                        
                        @schemas.classproperty
                        def H12(cls):
                            return cls("H12")
                        
                        @schemas.classproperty
                        def DAY(cls):
                            return cls("DAY")
                        
                        @schemas.classproperty
                        def WEEK(cls):
                            return cls("WEEK")
                        
                        @schemas.classproperty
                        def MONTH(cls):
                            return cls("MONTH")
                        
                        @schemas.classproperty
                        def QUARTER(cls):
                            return cls("QUARTER")
                        
                        @schemas.classproperty
                        def YEAR(cls):
                            return cls("YEAR")
                        
                        @schemas.classproperty
                        def DECADE(cls):
                            return cls("DECADE")
                        
                        @schemas.classproperty
                        def CENTURY(cls):
                            return cls("CENTURY")
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'aggregationRasters':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class viewer(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'viewer':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ar(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ar':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class sequence(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sequence':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class virtual(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'virtual':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class scale(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scale':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class zero(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'zero':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class map(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'map':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class sourcePath(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourcePath':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class isDigital(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'isDigital':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "name": name,
                "subtype": subtype,
                "assetTypeName": assetTypeName,
                "type": type,
                "enable": enable,
                "translation": translation,
                "unit": unit,
                "precision": precision,
                "min": min,
                "max": max,
                "aggregationMode": aggregationMode,
                "aggregationRasters": aggregationRasters,
                "viewer": viewer,
                "ar": ar,
                "sequence": sequence,
                "virtual": virtual,
                "scale": scale,
                "zero": zero,
                "map": map,
                "sourcePath": sourcePath,
                "isDigital": isDigital,
            }
    
    subtype: 'DataSubtype'
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subtype"]) -> 'DataSubtype': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetTypeName"]) -> MetaOapg.properties.assetTypeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable"]) -> MetaOapg.properties.enable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translation"]) -> 'Translation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["precision"]) -> MetaOapg.properties.precision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregationMode"]) -> MetaOapg.properties.aggregationMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregationRasters"]) -> MetaOapg.properties.aggregationRasters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewer"]) -> MetaOapg.properties.viewer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ar"]) -> MetaOapg.properties.ar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence"]) -> MetaOapg.properties.sequence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["virtual"]) -> MetaOapg.properties.virtual: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale"]) -> MetaOapg.properties.scale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zero"]) -> MetaOapg.properties.zero: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map"]) -> MetaOapg.properties.map: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourcePath"]) -> MetaOapg.properties.sourcePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDigital"]) -> MetaOapg.properties.isDigital: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "subtype", "assetTypeName", "type", "enable", "translation", "unit", "precision", "min", "max", "aggregationMode", "aggregationRasters", "viewer", "ar", "sequence", "virtual", "scale", "zero", "map", "sourcePath", "isDigital", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subtype"]) -> 'DataSubtype': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetTypeName"]) -> typing.Union[MetaOapg.properties.assetTypeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable"]) -> typing.Union[MetaOapg.properties.enable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translation"]) -> typing.Union['Translation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> typing.Union[MetaOapg.properties.unit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["precision"]) -> typing.Union[MetaOapg.properties.precision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> typing.Union[MetaOapg.properties.min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max"]) -> typing.Union[MetaOapg.properties.max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregationMode"]) -> typing.Union[MetaOapg.properties.aggregationMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregationRasters"]) -> typing.Union[MetaOapg.properties.aggregationRasters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewer"]) -> typing.Union[MetaOapg.properties.viewer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ar"]) -> typing.Union[MetaOapg.properties.ar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence"]) -> typing.Union[MetaOapg.properties.sequence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["virtual"]) -> typing.Union[MetaOapg.properties.virtual, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale"]) -> typing.Union[MetaOapg.properties.scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zero"]) -> typing.Union[MetaOapg.properties.zero, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map"]) -> typing.Union[MetaOapg.properties.map, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourcePath"]) -> typing.Union[MetaOapg.properties.sourcePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDigital"]) -> typing.Union[MetaOapg.properties.isDigital, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "subtype", "assetTypeName", "type", "enable", "translation", "unit", "precision", "min", "max", "aggregationMode", "aggregationRasters", "viewer", "ar", "sequence", "virtual", "scale", "zero", "map", "sourcePath", "isDigital", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        subtype: 'DataSubtype',
        name: typing.Union[MetaOapg.properties.name, str, ],
        assetTypeName: typing.Union[MetaOapg.properties.assetTypeName, None, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, None, str, schemas.Unset] = schemas.unset,
        enable: typing.Union[MetaOapg.properties.enable, bool, schemas.Unset] = schemas.unset,
        translation: typing.Union['Translation', schemas.Unset] = schemas.unset,
        unit: typing.Union[MetaOapg.properties.unit, None, str, schemas.Unset] = schemas.unset,
        precision: typing.Union[MetaOapg.properties.precision, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        min: typing.Union[MetaOapg.properties.min, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        max: typing.Union[MetaOapg.properties.max, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        aggregationMode: typing.Union[MetaOapg.properties.aggregationMode, None, str, schemas.Unset] = schemas.unset,
        aggregationRasters: typing.Union[MetaOapg.properties.aggregationRasters, list, tuple, schemas.Unset] = schemas.unset,
        viewer: typing.Union[MetaOapg.properties.viewer, None, bool, schemas.Unset] = schemas.unset,
        ar: typing.Union[MetaOapg.properties.ar, None, bool, schemas.Unset] = schemas.unset,
        sequence: typing.Union[MetaOapg.properties.sequence, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        virtual: typing.Union[MetaOapg.properties.virtual, None, bool, schemas.Unset] = schemas.unset,
        scale: typing.Union[MetaOapg.properties.scale, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        zero: typing.Union[MetaOapg.properties.zero, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        map: typing.Union[MetaOapg.properties.map, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        sourcePath: typing.Union[MetaOapg.properties.sourcePath, list, tuple, None, schemas.Unset] = schemas.unset,
        isDigital: typing.Union[MetaOapg.properties.isDigital, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssetTypeAttribute':
        return super().__new__(
            cls,
            *args,
            subtype=subtype,
            name=name,
            assetTypeName=assetTypeName,
            type=type,
            enable=enable,
            translation=translation,
            unit=unit,
            precision=precision,
            min=min,
            max=max,
            aggregationMode=aggregationMode,
            aggregationRasters=aggregationRasters,
            viewer=viewer,
            ar=ar,
            sequence=sequence,
            virtual=virtual,
            scale=scale,
            zero=zero,
            map=map,
            sourcePath=sourcePath,
            isDigital=isDigital,
            _configuration=_configuration,
            **kwargs,
        )

from eliona/api_client.model.data_subtype import DataSubtype
from eliona/api_client.model.translation import Translation

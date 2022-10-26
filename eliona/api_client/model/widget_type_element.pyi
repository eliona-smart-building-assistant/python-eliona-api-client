# coding: utf-8

"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.2.0
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


class WidgetTypeElement(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An element for widget types
    """


    class MetaOapg:
        required = {
            "description",
            "category",
        }
        
        class properties:
            
            
            class category(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INPUT(cls):
                    return cls("input")
                
                @schemas.classproperty
                def TABLE(cls):
                    return cls("table")
                
                @schemas.classproperty
                def IMAGE(cls):
                    return cls("image")
                
                @schemas.classproperty
                def TICKETS(cls):
                    return cls("tickets")
                
                @schemas.classproperty
                def MAP(cls):
                    return cls("map")
                
                @schemas.classproperty
                def ICON(cls):
                    return cls("icon")
                
                @schemas.classproperty
                def RANGE(cls):
                    return cls("range")
                
                @schemas.classproperty
                def DONUT(cls):
                    return cls("donut")
                
                @schemas.classproperty
                def COMFORT(cls):
                    return cls("comfort")
                
                @schemas.classproperty
                def SANKEY(cls):
                    return cls("sankey")
                
                @schemas.classproperty
                def PROGRESS(cls):
                    return cls("progress")
                
                @schemas.classproperty
                def TRACKING(cls):
                    return cls("tracking")
                
                @schemas.classproperty
                def HEATMAP(cls):
                    return cls("heatmap")
                
                @schemas.classproperty
                def RADAR(cls):
                    return cls("radar")
                
                @schemas.classproperty
                def VALUE(cls):
                    return cls("value")
                
                @schemas.classproperty
                def CALENDAR(cls):
                    return cls("calendar")
                
                @schemas.classproperty
                def TREND(cls):
                    return cls("trend")
                
                @schemas.classproperty
                def ALARMS(cls):
                    return cls("alarms")
                
                @schemas.classproperty
                def WEATHER(cls):
                    return cls("weather")
                
                @schemas.classproperty
                def STOREY(cls):
                    return cls("storey")
            
            
            class id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class sequence(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
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
            
            
            class config(
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
                ) -> 'config':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "category": category,
                "id": id,
                "sequence": sequence,
                "config": config,
            }
    
    description: schemas.AnyTypeSchema
    category: MetaOapg.properties.category
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence"]) -> MetaOapg.properties.sequence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["category", "id", "sequence", "config", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence"]) -> typing.Union[MetaOapg.properties.sequence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["category", "id", "sequence", "config", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        category: typing.Union[MetaOapg.properties.category, str, ],
        id: typing.Union[MetaOapg.properties.id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sequence: typing.Union[MetaOapg.properties.sequence, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        config: typing.Union[MetaOapg.properties.config, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WidgetTypeElement':
        return super().__new__(
            cls,
            *args,
            description=description,
            category=category,
            id=id,
            sequence=sequence,
            config=config,
            _configuration=_configuration,
            **kwargs,
        )
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


class WidgetType(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A frontend widget
    """


    class MetaOapg:
        required = {
            "elements",
            "name",
            "translation",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def translation() -> typing.Type['Translation']:
                return Translation
            
            
            class elements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WidgetTypeElement']:
                        return WidgetTypeElement
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WidgetTypeElement'], typing.List['WidgetTypeElement']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'elements':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WidgetTypeElement':
                    return super().__getitem__(i)
            
            
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
            custom = schemas.BoolSchema
            
            
            class icon(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'icon':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class withAlarm(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'withAlarm':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class withTimespan(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'withTimespan':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "name": name,
                "translation": translation,
                "elements": elements,
                "id": id,
                "custom": custom,
                "icon": icon,
                "withAlarm": withAlarm,
                "withTimespan": withTimespan,
            }
    
    elements: MetaOapg.properties.elements
    name: MetaOapg.properties.name
    translation: 'Translation'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translation"]) -> 'Translation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["elements"]) -> MetaOapg.properties.elements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom"]) -> MetaOapg.properties.custom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withAlarm"]) -> MetaOapg.properties.withAlarm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withTimespan"]) -> MetaOapg.properties.withTimespan: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "translation", "elements", "id", "custom", "icon", "withAlarm", "withTimespan", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translation"]) -> 'Translation': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["elements"]) -> MetaOapg.properties.elements: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom"]) -> typing.Union[MetaOapg.properties.custom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withAlarm"]) -> typing.Union[MetaOapg.properties.withAlarm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withTimespan"]) -> typing.Union[MetaOapg.properties.withTimespan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "translation", "elements", "id", "custom", "icon", "withAlarm", "withTimespan", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        elements: typing.Union[MetaOapg.properties.elements, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        translation: 'Translation',
        id: typing.Union[MetaOapg.properties.id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        custom: typing.Union[MetaOapg.properties.custom, bool, schemas.Unset] = schemas.unset,
        icon: typing.Union[MetaOapg.properties.icon, None, str, schemas.Unset] = schemas.unset,
        withAlarm: typing.Union[MetaOapg.properties.withAlarm, None, bool, schemas.Unset] = schemas.unset,
        withTimespan: typing.Union[MetaOapg.properties.withTimespan, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WidgetType':
        return super().__new__(
            cls,
            *args,
            elements=elements,
            name=name,
            translation=translation,
            id=id,
            custom=custom,
            icon=icon,
            withAlarm=withAlarm,
            withTimespan=withTimespan,
            _configuration=_configuration,
            **kwargs,
        )

from eliona/api_client.model.translation import Translation
from eliona/api_client.model.widget_type_element import WidgetTypeElement

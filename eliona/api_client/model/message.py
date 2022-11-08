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


class Message(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A message
    """


    class MetaOapg:
        required = {
            "recipients",
            "content",
        }
        
        class properties:
            
            
            class recipients(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'recipients':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            content = schemas.StrSchema
            
            
            class sender(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sender':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class copyRecipients(
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
                ) -> 'copyRecipients':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class blindCopyRecipients(
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
                ) -> 'blindCopyRecipients':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            subject = schemas.StrSchema
            
            
            class template(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "none": "NONE",
                        "eliona": "ELIONA",
                    }
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("none")
                
                @schemas.classproperty
                def ELIONA(cls):
                    return cls("eliona")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'template':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class attachments(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Attachment']:
                        return Attachment
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attachments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "recipients": recipients,
                "content": content,
                "sender": sender,
                "copyRecipients": copyRecipients,
                "blindCopyRecipients": blindCopyRecipients,
                "subject": subject,
                "template": template,
                "attachments": attachments,
            }
    
    recipients: MetaOapg.properties.recipients
    content: MetaOapg.properties.content
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipients"]) -> MetaOapg.properties.recipients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender"]) -> MetaOapg.properties.sender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyRecipients"]) -> MetaOapg.properties.copyRecipients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blindCopyRecipients"]) -> MetaOapg.properties.blindCopyRecipients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> MetaOapg.properties.template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["recipients", "content", "sender", "copyRecipients", "blindCopyRecipients", "subject", "template", "attachments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipients"]) -> MetaOapg.properties.recipients: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender"]) -> typing.Union[MetaOapg.properties.sender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyRecipients"]) -> typing.Union[MetaOapg.properties.copyRecipients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blindCopyRecipients"]) -> typing.Union[MetaOapg.properties.blindCopyRecipients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> typing.Union[MetaOapg.properties.template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["recipients", "content", "sender", "copyRecipients", "blindCopyRecipients", "subject", "template", "attachments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        recipients: typing.Union[MetaOapg.properties.recipients, list, tuple, ],
        content: typing.Union[MetaOapg.properties.content, str, ],
        sender: typing.Union[MetaOapg.properties.sender, None, str, schemas.Unset] = schemas.unset,
        copyRecipients: typing.Union[MetaOapg.properties.copyRecipients, list, tuple, None, schemas.Unset] = schemas.unset,
        blindCopyRecipients: typing.Union[MetaOapg.properties.blindCopyRecipients, list, tuple, None, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        template: typing.Union[MetaOapg.properties.template, None, str, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Message':
        return super().__new__(
            cls,
            *args,
            recipients=recipients,
            content=content,
            sender=sender,
            copyRecipients=copyRecipients,
            blindCopyRecipients=blindCopyRecipients,
            subject=subject,
            template=template,
            attachments=attachments,
            _configuration=_configuration,
            **kwargs,
        )

from eliona/api_client.model.attachment import Attachment

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


class AlarmPriority(
    schemas.EnumBase,
    schemas.IntSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The priority of the alarm. The higher this value the higher the priority.
    """
    
    @schemas.classproperty
    def ALARM_PRIORITY_LOW(cls):
        return cls(1)
    
    @schemas.classproperty
    def ALARM_PRIORITY_MEDIUM(cls):
        return cls(2)
    
    @schemas.classproperty
    def ALARM_PRIORITY_HEIGHT(cls):
        return cls(3)
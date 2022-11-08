# coding: utf-8

"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.4.2
    Generated by: https://openapi-generator.tech
"""

from eliona.api_client.paths.message_receipts_message_id.get import GetMessageReceiptById
from eliona.api_client.paths.send_mail.post import PostMail


class MessagesApi(
    GetMessageReceiptById,
    PostMail,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
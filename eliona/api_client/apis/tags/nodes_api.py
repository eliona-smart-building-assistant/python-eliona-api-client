# coding: utf-8

"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.4.2
    Generated by: https://openapi-generator.tech
"""

from eliona.api_client.paths.nodes_node_ident.get import GetNodeByIdent
from eliona.api_client.paths.nodes.get import GetNodes
from eliona.api_client.paths.nodes.post import PostNode
from eliona.api_client.paths.nodes.put import PutNode
from eliona.api_client.paths.nodes_node_ident.put import PutNodeByIdent


class NodesApi(
    GetNodeByIdent,
    GetNodes,
    PostNode,
    PutNode,
    PutNodeByIdent,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

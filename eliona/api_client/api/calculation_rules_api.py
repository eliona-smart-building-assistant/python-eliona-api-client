"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.  # noqa: E501

    The version of the OpenAPI document: 2.6.12
    Contact: hello@eliona.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eliona.api_client.api_client import ApiClient, Endpoint as _Endpoint
from eliona.api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from eliona.api_client.model.calculation_rule import CalculationRule


class CalculationRulesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_calculation_rule_by_id_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/calculation-rules/{calculation-rule-id}',
                'operation_id': 'delete_calculation_rule_by_id',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'calculation_rule_id',
                ],
                'required': [
                    'calculation_rule_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'calculation_rule_id':
                        (int,),
                },
                'attribute_map': {
                    'calculation_rule_id': 'calculation-rule-id',
                },
                'location_map': {
                    'calculation_rule_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_calculation_rule_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (CalculationRule,),
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/calculation-rules/{calculation-rule-id}',
                'operation_id': 'get_calculation_rule_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'calculation_rule_id',
                ],
                'required': [
                    'calculation_rule_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'calculation_rule_id':
                        (int,),
                },
                'attribute_map': {
                    'calculation_rule_id': 'calculation-rule-id',
                },
                'location_map': {
                    'calculation_rule_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_calculation_rules_endpoint = _Endpoint(
            settings={
                'response_type': ([CalculationRule],),
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/calculation-rules',
                'operation_id': 'get_calculation_rules',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'calculation_rule_ids',
                ],
                'required': [],
                'nullable': [
                    'calculation_rule_ids',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'calculation_rule_ids':
                        ([int], none_type,),
                },
                'attribute_map': {
                    'calculation_rule_ids': 'calculationRuleIds',
                },
                'location_map': {
                    'calculation_rule_ids': 'query',
                },
                'collection_format_map': {
                    'calculation_rule_ids': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.put_calculation_rule_endpoint = _Endpoint(
            settings={
                'response_type': (CalculationRule,),
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/calculation-rules',
                'operation_id': 'put_calculation_rule',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'calculation_rule',
                ],
                'required': [
                    'calculation_rule',
                ],
                'nullable': [
                    'calculation_rule',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'calculation_rule':
                        (CalculationRule,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'calculation_rule': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.put_calculation_rule_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (CalculationRule,),
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/calculation-rules/{calculation-rule-id}',
                'operation_id': 'put_calculation_rule_by_id',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'calculation_rule_id',
                    'calculation_rule',
                ],
                'required': [
                    'calculation_rule_id',
                    'calculation_rule',
                ],
                'nullable': [
                    'calculation_rule',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'calculation_rule_id':
                        (int,),
                    'calculation_rule':
                        (CalculationRule,),
                },
                'attribute_map': {
                    'calculation_rule_id': 'calculation-rule-id',
                },
                'location_map': {
                    'calculation_rule_id': 'path',
                    'calculation_rule': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def delete_calculation_rule_by_id(
        self,
        calculation_rule_id,
        **kwargs
    ):
        """Delete a calculation rule  # noqa: E501

        Deletes a calculation rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_calculation_rule_by_id(calculation_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            calculation_rule_id (int): The id of the calculation rule

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['calculation_rule_id'] = \
            calculation_rule_id
        return self.delete_calculation_rule_by_id_endpoint.call_with_http_info(**kwargs)

    def get_calculation_rule_by_id(
        self,
        calculation_rule_id,
        **kwargs
    ):
        """Information about a calculation rules rule  # noqa: E501

        Gets information about a calculation rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_calculation_rule_by_id(calculation_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            calculation_rule_id (int): The id of the calculation rule

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CalculationRule
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['calculation_rule_id'] = \
            calculation_rule_id
        return self.get_calculation_rule_by_id_endpoint.call_with_http_info(**kwargs)

    def get_calculation_rules(
        self,
        **kwargs
    ):
        """Information about calculation rules  # noqa: E501

        Gets information about calculation rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_calculation_rules(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            calculation_rule_ids ([int], none_type): List of calculation rule ids for filtering. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [CalculationRule]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_calculation_rules_endpoint.call_with_http_info(**kwargs)

    def put_calculation_rule(
        self,
        calculation_rule,
        **kwargs
    ):
        """Creates or updates a calculation rule  # noqa: E501

        Creates a new or updates an existing calculation rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_calculation_rule(calculation_rule, async_req=True)
        >>> result = thread.get()

        Args:
            calculation_rule (CalculationRule):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CalculationRule
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['calculation_rule'] = \
            calculation_rule
        return self.put_calculation_rule_endpoint.call_with_http_info(**kwargs)

    def put_calculation_rule_by_id(
        self,
        calculation_rule_id,
        calculation_rule,
        **kwargs
    ):
        """Update a calculation rule  # noqa: E501

        Update a calculation rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_calculation_rule_by_id(calculation_rule_id, calculation_rule, async_req=True)
        >>> result = thread.get()

        Args:
            calculation_rule_id (int): The id of the calculation rule
            calculation_rule (CalculationRule):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CalculationRule
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['calculation_rule_id'] = \
            calculation_rule_id
        kwargs['calculation_rule'] = \
            calculation_rule
        return self.put_calculation_rule_by_id_endpoint.call_with_http_info(**kwargs)


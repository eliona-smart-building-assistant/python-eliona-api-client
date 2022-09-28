"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eliona.api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from eliona.api_client.exceptions import ApiAttributeError


def lazy_import():
    from eliona.api_client.model.data_subtype import DataSubtype
    globals()['DataSubtype'] = DataSubtype


class DataAggregated(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('raster',): {
            'S1': "S1",
            'S2': "S2",
            'S3': "S3",
            'S4': "S4",
            'S5': "S5",
            'S6': "S6",
            'S10': "S10",
            'S12': "S12",
            'S15': "S15",
            'S20': "S20",
            'S30': "S30",
            'M1': "M1",
            'M2': "M2",
            'M3': "M3",
            'M4': "M4",
            'M5': "M5",
            'M6': "M6",
            'M10': "M10",
            'M12': "M12",
            'M15': "M15",
            'M20': "M20",
            'M30': "M30",
            'H1': "H1",
            'H2': "H2",
            'H3': "H3",
            'H4': "H4",
            'H6': "H6",
            'H8': "H8",
            'H12': "H12",
            'DAY': "DAY",
            'WEEK': "WEEK",
            'MONTH': "MONTH",
            'QUARTER': "QUARTER",
            'YEAR': "YEAR",
            'DECADE': "DECADE",
            'CENTURY': "CENTURY",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'asset_id': (int,),  # noqa: E501
            'subtype': (DataSubtype,),  # noqa: E501
            'raster': (str,),  # noqa: E501
            'aggregation_id': (int,),  # noqa: E501
            'attribute': (str,),  # noqa: E501
            'timestamp': (datetime, none_type,),  # noqa: E501
            'count': (float, none_type,),  # noqa: E501
            'average': (float, none_type,),  # noqa: E501
            'sum': (float, none_type,),  # noqa: E501
            'first': (float, none_type,),  # noqa: E501
            'min': (float, none_type,),  # noqa: E501
            'max': (float, none_type,),  # noqa: E501
            'last': (float, none_type,),  # noqa: E501
            'last_timestamp': (datetime, none_type,),  # noqa: E501
            'asset_type_name': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'asset_id': 'assetId',  # noqa: E501
        'subtype': 'subtype',  # noqa: E501
        'raster': 'raster',  # noqa: E501
        'aggregation_id': 'aggregationId',  # noqa: E501
        'attribute': 'attribute',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'count': 'count',  # noqa: E501
        'average': 'average',  # noqa: E501
        'sum': 'sum',  # noqa: E501
        'first': 'first',  # noqa: E501
        'min': 'min',  # noqa: E501
        'max': 'max',  # noqa: E501
        'last': 'last',  # noqa: E501
        'last_timestamp': 'lastTimestamp',  # noqa: E501
        'asset_type_name': 'assetTypeName',  # noqa: E501
    }

    read_only_vars = {
        'asset_type_name',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, asset_id, subtype, raster, *args, **kwargs):  # noqa: E501
        """DataAggregated - a model defined in OpenAPI

        Args:
            asset_id (int): ID of the corresponding asset
            subtype (DataSubtype):
            raster (str): Calculation intervals.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            aggregation_id (int): ID of the aggregation. [optional]  # noqa: E501
            attribute (str): Name of the attribute which holds the data points. [optional]  # noqa: E501
            timestamp (datetime, none_type): Timestamp of this aggregated data set. [optional]  # noqa: E501
            count (float, none_type): Count of data points in this aggregated data set. [optional]  # noqa: E501
            average (float, none_type): Average of all data points for this aggregated data set. [optional]  # noqa: E501
            sum (float, none_type): Sum of all data points for this aggregated data set. [optional]  # noqa: E501
            first (float, none_type): First data point in this aggregated data set. [optional]  # noqa: E501
            min (float, none_type): Data point with the most minimal value in this aggregated data set. [optional]  # noqa: E501
            max (float, none_type): Data point with the most maximal value in this aggregated data set. [optional]  # noqa: E501
            last (float, none_type): Latest data point in this aggregated data set. [optional]  # noqa: E501
            last_timestamp (datetime, none_type): Timestamp of the latest data point. [optional]  # noqa: E501
            asset_type_name (str, none_type): The name of the corresponding asset type. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.asset_id = asset_id
        self.subtype = subtype
        self.raster = raster
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, asset_id, subtype, raster, *args, **kwargs):  # noqa: E501
        """DataAggregated - a model defined in OpenAPI

        Args:
            asset_id (int): ID of the corresponding asset
            subtype (DataSubtype):
            raster (str): Calculation intervals.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            aggregation_id (int): ID of the aggregation. [optional]  # noqa: E501
            attribute (str): Name of the attribute which holds the data points. [optional]  # noqa: E501
            timestamp (datetime, none_type): Timestamp of this aggregated data set. [optional]  # noqa: E501
            count (float, none_type): Count of data points in this aggregated data set. [optional]  # noqa: E501
            average (float, none_type): Average of all data points for this aggregated data set. [optional]  # noqa: E501
            sum (float, none_type): Sum of all data points for this aggregated data set. [optional]  # noqa: E501
            first (float, none_type): First data point in this aggregated data set. [optional]  # noqa: E501
            min (float, none_type): Data point with the most minimal value in this aggregated data set. [optional]  # noqa: E501
            max (float, none_type): Data point with the most maximal value in this aggregated data set. [optional]  # noqa: E501
            last (float, none_type): Latest data point in this aggregated data set. [optional]  # noqa: E501
            last_timestamp (datetime, none_type): Timestamp of the latest data point. [optional]  # noqa: E501
            asset_type_name (str, none_type): The name of the corresponding asset type. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.asset_id = asset_id
        self.subtype = subtype
        self.raster = raster
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
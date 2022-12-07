# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_19 import models

class ArrayConnectionPath(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'local_port': 'str',
        'local_address': 'str',
        'remote_port': 'str',
        'remote_address': 'str',
        'status': 'str',
        'replication_transport': 'str'
    }

    attribute_map = {
        'name': 'name',
        'local_port': 'local_port',
        'local_address': 'local_address',
        'remote_port': 'remote_port',
        'remote_address': 'remote_address',
        'status': 'status',
        'replication_transport': 'replication_transport'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        local_port=None,  # type: str
        local_address=None,  # type: str
        remote_port=None,  # type: str
        remote_address=None,  # type: str
        status=None,  # type: str
        replication_transport=None,  # type: str
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified.
            local_port (str): The local port of the path.
            local_address (str): IP address or WWN of the local port.
            remote_port (str): The remote port of the path.
            remote_address (str): IP address or WWN of the remote port.
            status (str): Status of the connection. Valid values are `connected` and `connecting`. A status of `connected` indicates that the arrays are communicating. A status of `connecting` indicates that the array is trying to establish a connection.
            replication_transport (str): The protocol used to transport data between the local array and the remote array. Valid values are `ip` and `fc`.
        """
        if name is not None:
            self.name = name
        if local_port is not None:
            self.local_port = local_port
        if local_address is not None:
            self.local_address = local_address
        if remote_port is not None:
            self.remote_port = remote_port
        if remote_address is not None:
            self.remote_address = remote_address
        if status is not None:
            self.status = status
        if replication_transport is not None:
            self.replication_transport = replication_transport

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnectionPath`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(ArrayConnectionPath, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArrayConnectionPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

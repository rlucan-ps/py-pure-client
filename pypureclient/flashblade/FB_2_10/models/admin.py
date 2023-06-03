# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.10, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_10 import models

class Admin(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'api_token': 'ApiToken',
        'is_local': 'bool',
        'public_key': 'str',
        'role': 'Reference',
        'locked': 'bool',
        'lockout_remaining': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'api_token': 'api_token',
        'is_local': 'is_local',
        'public_key': 'public_key',
        'role': 'role',
        'locked': 'locked',
        'lockout_remaining': 'lockout_remaining'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        api_token=None,  # type: models.ApiToken
        is_local=None,  # type: bool
        public_key=None,  # type: str
        role=None,  # type: models.Reference
        locked=None,  # type: bool
        lockout_remaining=None,  # type: int
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            api_token (ApiToken)
            is_local (bool): Returns a value of `true` if the user is local to the machine, otherwise `false`.
            public_key (str): Public key for SSH access. Supported key types are `Ed25519` and `RSA`.
            role (Reference): A reference to this administrator's management role.
            locked (bool): Returns a value of `true` if the user is currently locked out, otherwise `false`. Can be patched to false to unlock a user. This field is only visible to `array_admin` roles. For all other users, the value is always `null`.
            lockout_remaining (int): The remaining lockout period, in milliseconds, if the user is locked out. This field is only visible to `array_admin` roles. For all other users, the value is always `null`.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if api_token is not None:
            self.api_token = api_token
        if is_local is not None:
            self.is_local = is_local
        if public_key is not None:
            self.public_key = public_key
        if role is not None:
            self.role = role
        if locked is not None:
            self.locked = locked
        if lockout_remaining is not None:
            self.lockout_remaining = lockout_remaining

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Admin`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
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
        if issubclass(Admin, dict):
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
        if not isinstance(other, Admin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

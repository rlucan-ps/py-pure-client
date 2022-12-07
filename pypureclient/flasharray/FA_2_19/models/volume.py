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

class Volume(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'connection_count': 'int',
        'created': 'int',
        'destroyed': 'bool',
        'host_encryption_key_status': 'str',
        'priority_adjustment': 'PriorityAdjustment',
        'provisioned': 'int',
        'qos': 'Qos',
        'serial': 'str',
        'space': 'VolumeSpaceCommon',
        'time_remaining': 'int',
        'pod': 'Reference',
        'priority': 'int',
        'promotion_status': 'str',
        'requested_promotion_state': 'str',
        'source': 'FixedReference',
        'subtype': 'str',
        'volume_group': 'Reference'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'connection_count': 'connection_count',
        'created': 'created',
        'destroyed': 'destroyed',
        'host_encryption_key_status': 'host_encryption_key_status',
        'priority_adjustment': 'priority_adjustment',
        'provisioned': 'provisioned',
        'qos': 'qos',
        'serial': 'serial',
        'space': 'space',
        'time_remaining': 'time_remaining',
        'pod': 'pod',
        'priority': 'priority',
        'promotion_status': 'promotion_status',
        'requested_promotion_state': 'requested_promotion_state',
        'source': 'source',
        'subtype': 'subtype',
        'volume_group': 'volume_group'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        connection_count=None,  # type: int
        created=None,  # type: int
        destroyed=None,  # type: bool
        host_encryption_key_status=None,  # type: str
        priority_adjustment=None,  # type: models.PriorityAdjustment
        provisioned=None,  # type: int
        qos=None,  # type: models.Qos
        serial=None,  # type: str
        space=None,  # type: models.VolumeSpaceCommon
        time_remaining=None,  # type: int
        pod=None,  # type: models.Reference
        priority=None,  # type: int
        promotion_status=None,  # type: str
        requested_promotion_state=None,  # type: str
        source=None,  # type: models.FixedReference
        subtype=None,  # type: str
        volume_group=None,  # type: models.Reference
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            connection_count (int): The total number of hosts and host groups connected to the volume.
            created (int): The volume creation time, measured in milliseconds since the UNIX epoch.
            destroyed (bool): Returns a value of `true` if the volume has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed volume is permanently eradicated. Before the `time_remaining` period has elapsed, the destroyed volume can be recovered by setting `destroyed=false`. Once the `time_remaining` period has elapsed, the volume is permanently eradicated and can no longer be recovered.
            host_encryption_key_status (str): The host encryption key status for this volume. Possible values include `none`, `detected`, and `fetched`.
            priority_adjustment (PriorityAdjustment): Priority adjustment operator and value.
            provisioned (int): The virtual size of the volume as a multiple of 512, measured in bytes. The maximum size is 4503599627370496 (4PB)
            qos (Qos): Displays QoS limit information.
            serial (str): A globally unique serial number generated by the FlashArray when the volume is created.
            space (VolumeSpaceCommon): Displays size and space consumption information.
            time_remaining (int): The amount of time left until the destroyed volume is permanently eradicated, measured in milliseconds. Before the `time_remaining` period has elapsed, the destroyed volume can be recovered by setting `destroyed=false`.
            pod (Reference): A reference to the pod.
            priority (int): Current priority value. Priority is calculated by combining all applicable relative `priority_adjustment` values or taking the exact value if the volume has an absolute `priority_adjustment` (specified by an `=` `priority_adjustment_operator`).
            promotion_status (str): Current promotion status of a volume. Valid values are `promoted` and `demoted`. A status of `promoted` indicates that the volume has been promoted and can accept write requests from hosts. This is the default status for a volume when it is created. A status of `demoted` indicates that the volume has been demoted and no longer accepts write requests.
            requested_promotion_state (str): Valid values are `promoted` and `demoted`. Patch `requested_promotion_state` to `demoted` to demote the volume so that the volume stops accepting write requests. Patch `requested_promotion_state` to `promoted` to promote the volume so that the volume starts accepting write requests.
            source (FixedReference): A reference to the originating volume as a result of a volume copy.
            subtype (str): The type of volume. Valid values are `protocol_endpoint` and `regular`.
            volume_group (Reference): A reference to the volume group.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if connection_count is not None:
            self.connection_count = connection_count
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if host_encryption_key_status is not None:
            self.host_encryption_key_status = host_encryption_key_status
        if priority_adjustment is not None:
            self.priority_adjustment = priority_adjustment
        if provisioned is not None:
            self.provisioned = provisioned
        if qos is not None:
            self.qos = qos
        if serial is not None:
            self.serial = serial
        if space is not None:
            self.space = space
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if pod is not None:
            self.pod = pod
        if priority is not None:
            self.priority = priority
        if promotion_status is not None:
            self.promotion_status = promotion_status
        if requested_promotion_state is not None:
            self.requested_promotion_state = requested_promotion_state
        if source is not None:
            self.source = source
        if subtype is not None:
            self.subtype = subtype
        if volume_group is not None:
            self.volume_group = volume_group

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Volume`".format(key))
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
        if issubclass(Volume, dict):
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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

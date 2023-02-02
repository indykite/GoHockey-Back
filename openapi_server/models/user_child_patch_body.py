# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserChildPatchBody(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cloth_size=None, shoe_size=None, helmet_size=None):  # noqa: E501
        """UserChildPatchBody - a model defined in OpenAPI

        :param cloth_size: The cloth_size of this UserChildPatchBody.  # noqa: E501
        :type cloth_size: str
        :param shoe_size: The shoe_size of this UserChildPatchBody.  # noqa: E501
        :type shoe_size: str
        :param helmet_size: The helmet_size of this UserChildPatchBody.  # noqa: E501
        :type helmet_size: str
        """
        self.openapi_types = {
            'cloth_size': str,
            'shoe_size': str,
            'helmet_size': str
        }

        self.attribute_map = {
            'cloth_size': 'cloth_size',
            'shoe_size': 'shoe_size',
            'helmet_size': 'helmet_size'
        }

        self._cloth_size = cloth_size
        self._shoe_size = shoe_size
        self._helmet_size = helmet_size

    @classmethod
    def from_dict(cls, dikt) -> 'UserChildPatchBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_child_patch_body of this UserChildPatchBody.  # noqa: E501
        :rtype: UserChildPatchBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cloth_size(self):
        """Gets the cloth_size of this UserChildPatchBody.


        :return: The cloth_size of this UserChildPatchBody.
        :rtype: str
        """
        return self._cloth_size

    @cloth_size.setter
    def cloth_size(self, cloth_size):
        """Sets the cloth_size of this UserChildPatchBody.


        :param cloth_size: The cloth_size of this UserChildPatchBody.
        :type cloth_size: str
        """

        self._cloth_size = cloth_size

    @property
    def shoe_size(self):
        """Gets the shoe_size of this UserChildPatchBody.


        :return: The shoe_size of this UserChildPatchBody.
        :rtype: str
        """
        return self._shoe_size

    @shoe_size.setter
    def shoe_size(self, shoe_size):
        """Sets the shoe_size of this UserChildPatchBody.


        :param shoe_size: The shoe_size of this UserChildPatchBody.
        :type shoe_size: str
        """

        self._shoe_size = shoe_size

    @property
    def helmet_size(self):
        """Gets the helmet_size of this UserChildPatchBody.


        :return: The helmet_size of this UserChildPatchBody.
        :rtype: str
        """
        return self._helmet_size

    @helmet_size.setter
    def helmet_size(self, helmet_size):
        """Sets the helmet_size of this UserChildPatchBody.


        :param helmet_size: The helmet_size of this UserChildPatchBody.
        :type helmet_size: str
        """

        self._helmet_size = helmet_size
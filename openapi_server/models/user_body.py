# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserBody(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email=None, name=None):  # noqa: E501
        """UserBody - a model defined in OpenAPI

        :param email: The email of this UserBody.  # noqa: E501
        :type email: str
        :param name: The name of this UserBody.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'email': str,
            'name': str
        }

        self.attribute_map = {
            'email': 'email',
            'name': 'name'
        }

        self._email = email
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'UserBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_body of this UserBody.  # noqa: E501
        :rtype: UserBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self):
        """Gets the email of this UserBody.


        :return: The email of this UserBody.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserBody.


        :param email: The email of this UserBody.
        :type email: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this UserBody.


        :return: The name of this UserBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserBody.


        :param name: The name of this UserBody.
        :type name: str
        """

        self._name = name

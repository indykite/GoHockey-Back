# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserChildBody(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, given_name=None, year_of_birth=None, gender=None, cloth_size=None, shoe_size=None, helmet_size=None):  # noqa: E501
        """UserChildBody - a model defined in OpenAPI

        :param given_name: The given_name of this UserChildBody.  # noqa: E501
        :type given_name: str
        :param year_of_birth: The year_of_birth of this UserChildBody.  # noqa: E501
        :type year_of_birth: str
        :param gender: The gender of this UserChildBody.  # noqa: E501
        :type gender: str
        :param cloth_size: The cloth_size of this UserChildBody.  # noqa: E501
        :type cloth_size: str
        :param shoe_size: The shoe_size of this UserChildBody.  # noqa: E501
        :type shoe_size: str
        :param helmet_size: The helmet_size of this UserChildBody.  # noqa: E501
        :type helmet_size: str
        """
        self.openapi_types = {
            'given_name': str,
            'year_of_birth': str,
            'gender': str,
            'cloth_size': str,
            'shoe_size': str,
            'helmet_size': str
        }

        self.attribute_map = {
            'given_name': 'given_name',
            'year_of_birth': 'year_of_birth',
            'gender': 'gender',
            'cloth_size': 'cloth_size',
            'shoe_size': 'shoe_size',
            'helmet_size': 'helmet_size'
        }

        self._given_name = given_name
        self._year_of_birth = year_of_birth
        self._gender = gender
        self._cloth_size = cloth_size
        self._shoe_size = shoe_size
        self._helmet_size = helmet_size

    @classmethod
    def from_dict(cls, dikt) -> 'UserChildBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_child_body of this UserChildBody.  # noqa: E501
        :rtype: UserChildBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def given_name(self):
        """Gets the given_name of this UserChildBody.


        :return: The given_name of this UserChildBody.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this UserChildBody.


        :param given_name: The given_name of this UserChildBody.
        :type given_name: str
        """

        self._given_name = given_name

    @property
    def year_of_birth(self):
        """Gets the year_of_birth of this UserChildBody.


        :return: The year_of_birth of this UserChildBody.
        :rtype: str
        """
        return self._year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        """Sets the year_of_birth of this UserChildBody.


        :param year_of_birth: The year_of_birth of this UserChildBody.
        :type year_of_birth: str
        """

        self._year_of_birth = year_of_birth

    @property
    def gender(self):
        """Gets the gender of this UserChildBody.


        :return: The gender of this UserChildBody.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this UserChildBody.


        :param gender: The gender of this UserChildBody.
        :type gender: str
        """

        self._gender = gender

    @property
    def cloth_size(self):
        """Gets the cloth_size of this UserChildBody.


        :return: The cloth_size of this UserChildBody.
        :rtype: str
        """
        return self._cloth_size

    @cloth_size.setter
    def cloth_size(self, cloth_size):
        """Sets the cloth_size of this UserChildBody.


        :param cloth_size: The cloth_size of this UserChildBody.
        :type cloth_size: str
        """

        self._cloth_size = cloth_size

    @property
    def shoe_size(self):
        """Gets the shoe_size of this UserChildBody.


        :return: The shoe_size of this UserChildBody.
        :rtype: str
        """
        return self._shoe_size

    @shoe_size.setter
    def shoe_size(self, shoe_size):
        """Sets the shoe_size of this UserChildBody.


        :param shoe_size: The shoe_size of this UserChildBody.
        :type shoe_size: str
        """

        self._shoe_size = shoe_size

    @property
    def helmet_size(self):
        """Gets the helmet_size of this UserChildBody.


        :return: The helmet_size of this UserChildBody.
        :rtype: str
        """
        return self._helmet_size

    @helmet_size.setter
    def helmet_size(self, helmet_size):
        """Sets the helmet_size of this UserChildBody.


        :param helmet_size: The helmet_size of this UserChildBody.
        :type helmet_size: str
        """

        self._helmet_size = helmet_size

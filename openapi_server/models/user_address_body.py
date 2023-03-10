# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserAddressBody(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, street=None, city=None, country=None, zip=None):  # noqa: E501
        """UserAddressBody - a model defined in OpenAPI

        :param street: The street of this UserAddressBody.  # noqa: E501
        :type street: str
        :param city: The city of this UserAddressBody.  # noqa: E501
        :type city: str
        :param country: The country of this UserAddressBody.  # noqa: E501
        :type country: str
        :param zip: The zip of this UserAddressBody.  # noqa: E501
        :type zip: str
        """
        self.openapi_types = {
            'street': str,
            'city': str,
            'country': str,
            'zip': str
        }

        self.attribute_map = {
            'street': 'street',
            'city': 'city',
            'country': 'country',
            'zip': 'zip'
        }

        self._street = street
        self._city = city
        self._country = country
        self._zip = zip

    @classmethod
    def from_dict(cls, dikt) -> 'UserAddressBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_address_body of this UserAddressBody.  # noqa: E501
        :rtype: UserAddressBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def street(self):
        """Gets the street of this UserAddressBody.


        :return: The street of this UserAddressBody.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this UserAddressBody.


        :param street: The street of this UserAddressBody.
        :type street: str
        """

        self._street = street

    @property
    def city(self):
        """Gets the city of this UserAddressBody.


        :return: The city of this UserAddressBody.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this UserAddressBody.


        :param city: The city of this UserAddressBody.
        :type city: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this UserAddressBody.


        :return: The country of this UserAddressBody.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UserAddressBody.


        :param country: The country of this UserAddressBody.
        :type country: str
        """

        self._country = country

    @property
    def zip(self):
        """Gets the zip of this UserAddressBody.


        :return: The zip of this UserAddressBody.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this UserAddressBody.


        :param zip: The zip of this UserAddressBody.
        :type zip: str
        """

        self._zip = zip

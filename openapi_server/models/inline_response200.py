# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, street=None, number=None, city=None, state=None, zip=None, country=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param street: The street of this InlineResponse200.  # noqa: E501
        :type street: str
        :param number: The number of this InlineResponse200.  # noqa: E501
        :type number: int
        :param city: The city of this InlineResponse200.  # noqa: E501
        :type city: str
        :param state: The state of this InlineResponse200.  # noqa: E501
        :type state: str
        :param zip: The zip of this InlineResponse200.  # noqa: E501
        :type zip: str
        :param country: The country of this InlineResponse200.  # noqa: E501
        :type country: str
        """
        self.openapi_types = {
            'street': str,
            'number': int,
            'city': str,
            'state': str,
            'zip': str,
            'country': str
        }

        self.attribute_map = {
            'street': 'street',
            'number': 'number',
            'city': 'city',
            'state': 'state',
            'zip': 'zip',
            'country': 'country'
        }

        self._street = street
        self._number = number
        self._city = city
        self._state = state
        self._zip = zip
        self._country = country

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def street(self):
        """Gets the street of this InlineResponse200.


        :return: The street of this InlineResponse200.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this InlineResponse200.


        :param street: The street of this InlineResponse200.
        :type street: str
        """

        self._street = street

    @property
    def number(self):
        """Gets the number of this InlineResponse200.


        :return: The number of this InlineResponse200.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineResponse200.


        :param number: The number of this InlineResponse200.
        :type number: int
        """

        self._number = number

    @property
    def city(self):
        """Gets the city of this InlineResponse200.


        :return: The city of this InlineResponse200.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this InlineResponse200.


        :param city: The city of this InlineResponse200.
        :type city: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this InlineResponse200.


        :return: The state of this InlineResponse200.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineResponse200.


        :param state: The state of this InlineResponse200.
        :type state: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this InlineResponse200.


        :return: The zip of this InlineResponse200.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this InlineResponse200.


        :param zip: The zip of this InlineResponse200.
        :type zip: str
        """

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this InlineResponse200.


        :return: The country of this InlineResponse200.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InlineResponse200.


        :param country: The country of this InlineResponse200.
        :type country: str
        """

        self._country = country
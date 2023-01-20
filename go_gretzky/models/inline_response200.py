# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from go_gretzky.models.base_model_ import Model
from go_gretzky import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, street: str=None, number: int=None, city: str=None, state: str=None, zip: str=None, country: str=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

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
        self.swagger_types = {
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
    def street(self) -> str:
        """Gets the street of this InlineResponse200.


        :return: The street of this InlineResponse200.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """Sets the street of this InlineResponse200.


        :param street: The street of this InlineResponse200.
        :type street: str
        """

        self._street = street

    @property
    def number(self) -> int:
        """Gets the number of this InlineResponse200.


        :return: The number of this InlineResponse200.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number: int):
        """Sets the number of this InlineResponse200.


        :param number: The number of this InlineResponse200.
        :type number: int
        """

        self._number = number

    @property
    def city(self) -> str:
        """Gets the city of this InlineResponse200.


        :return: The city of this InlineResponse200.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this InlineResponse200.


        :param city: The city of this InlineResponse200.
        :type city: str
        """

        self._city = city

    @property
    def state(self) -> str:
        """Gets the state of this InlineResponse200.


        :return: The state of this InlineResponse200.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this InlineResponse200.


        :param state: The state of this InlineResponse200.
        :type state: str
        """

        self._state = state

    @property
    def zip(self) -> str:
        """Gets the zip of this InlineResponse200.


        :return: The zip of this InlineResponse200.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip: str):
        """Sets the zip of this InlineResponse200.


        :param zip: The zip of this InlineResponse200.
        :type zip: str
        """

        self._zip = zip

    @property
    def country(self) -> str:
        """Gets the country of this InlineResponse200.


        :return: The country of this InlineResponse200.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this InlineResponse200.


        :param country: The country of this InlineResponse200.
        :type country: str
        """

        self._country = country

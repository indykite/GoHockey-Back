# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.user_address_body import UserAddressBody  # noqa: E501
from openapi_server.models.user_child_body import UserChildBody  # noqa: E501
from openapi_server.models.user_subscription_body import UserSubscriptionBody  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_user_address_get(self):
        """Test case for user_address_get

        Get the home address of the logged in user
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/user/address',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_address_post(self):
        """Test case for user_address_post

        Add a home address to the logged in user
        """
        user_address_body = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/user/address',
            method='POST',
            headers=headers,
            data=json.dumps(user_address_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_child_child_id_get(self):
        """Test case for user_child_child_id_get

        Get the child by id
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/user/child/{child_id}'.format(child_id='child_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_child_post(self):
        """Test case for user_child_post

        Add a child to the logged in user
        """
        user_child_body = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/user/child',
            method='POST',
            headers=headers,
            data=json.dumps(user_child_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_email_get(self):
        """Test case for user_email_get

        Get the email of the logged in user
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/user/email',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_subscription_get(self):
        """Test case for user_subscription_get

        Get the subscription of the logged in user
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/user/subscription',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_subscription_post(self):
        """Test case for user_subscription_post

        Add a subscription to the logged in user
        """
        user_subscription_body = {}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/user/subscription',
            method='POST',
            headers=headers,
            data=json.dumps(user_subscription_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from go_gretzky.models.inline_response200 import InlineResponse200  # noqa: E501
from go_gretzky.models.inline_response2001 import InlineResponse2001  # noqa: E501
from go_gretzky.models.user_address_body import UserAddressBody  # noqa: E501
from go_gretzky.models.user_child_body import UserChildBody  # noqa: E501
from go_gretzky.models.user_subscription_body import UserSubscriptionBody  # noqa: E501
from go_gretzky.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_user_address_get(self):
        """Test case for user_address_get

        Get the home address of the logged in user
        """
        response = self.client.open(
            '/user/address',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_address_post(self):
        """Test case for user_address_post

        Add a home address to the logged in user
        """
        body = UserAddressBody()
        response = self.client.open(
            '/user/address',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_child_child_id_get(self):
        """Test case for user_child_child_id_get

        Get the child by id
        """
        response = self.client.open(
            '/user/child/{childId}'.format(child_id='child_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_child_post(self):
        """Test case for user_child_post

        Add a child to the logged in user
        """
        body = UserChildBody()
        response = self.client.open(
            '/user/child',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_email_get(self):
        """Test case for user_email_get

        Get the email of the logged in user
        """
        response = self.client.open(
            '/user/email',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_subscription_get(self):
        """Test case for user_subscription_get

        Get the subscription of the logged in user
        """
        response = self.client.open(
            '/user/subscription',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_subscription_post(self):
        """Test case for user_subscription_post

        Add a subscription to the logged in user
        """
        body = UserSubscriptionBody()
        response = self.client.open(
            '/user/subscription',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

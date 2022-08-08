"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergeTicketingClient
from MergeTicketingClient.model.remote_data import RemoteData
globals()['RemoteData'] = RemoteData
from MergeTicketingClient.model.user import User
from MergeTicketingClient.api_client import ApiClient


class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUser(self):
        """Test User"""
        # FIXME: construct object with mandatory attributes with example values
        # model = User()  # noqa: E501

        """
        No test json responses were defined for User
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (User,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()

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
from MergeTicketingClient.model.patched_ticket_request import PatchedTicketRequest
from MergeTicketingClient.api_client import ApiClient


class TestPatchedTicketRequest(unittest.TestCase):
    """PatchedTicketRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPatchedTicketRequest(self):
        """Test PatchedTicketRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PatchedTicketRequest()  # noqa: E501

        """
        No test json responses were defined for PatchedTicketRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PatchedTicketRequest,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()

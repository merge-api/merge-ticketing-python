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
from MergeTicketingClient.model.ticket_request import TicketRequest
globals()['TicketRequest'] = TicketRequest
from MergeTicketingClient.model.ticket_endpoint_request import TicketEndpointRequest
from MergeTicketingClient.api_client import ApiClient


class TestTicketEndpointRequest(unittest.TestCase):
    """TicketEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTicketEndpointRequest(self):
        """Test TicketEndpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TicketEndpointRequest()  # noqa: E501

        """
        No test json responses were defined for TicketEndpointRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (TicketEndpointRequest,), False)

        assert deserialized is not None

        assert deserialized.model is not None


if __name__ == '__main__':
    unittest.main()

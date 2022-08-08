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
from MergeTicketingClient.model.attachment_request import AttachmentRequest
globals()['AttachmentRequest'] = AttachmentRequest
from MergeTicketingClient.model.ticketing_attachment_endpoint_request import TicketingAttachmentEndpointRequest
from MergeTicketingClient.api_client import ApiClient


class TestTicketingAttachmentEndpointRequest(unittest.TestCase):
    """TicketingAttachmentEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTicketingAttachmentEndpointRequest(self):
        """Test TicketingAttachmentEndpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TicketingAttachmentEndpointRequest()  # noqa: E501

        """
        No test json responses were defined for TicketingAttachmentEndpointRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (TicketingAttachmentEndpointRequest,), False)

        assert deserialized is not None

        assert deserialized.model is not None


if __name__ == '__main__':
    unittest.main()

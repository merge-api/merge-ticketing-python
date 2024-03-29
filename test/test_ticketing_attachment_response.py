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
from MergeTicketingClient.model.attachment import Attachment
from MergeTicketingClient.model.debug_mode_log import DebugModeLog
from MergeTicketingClient.model.error_validation_problem import ErrorValidationProblem
from MergeTicketingClient.model.warning_validation_problem import WarningValidationProblem
globals()['Attachment'] = Attachment
globals()['DebugModeLog'] = DebugModeLog
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergeTicketingClient.model.ticketing_attachment_response import TicketingAttachmentResponse
from MergeTicketingClient.api_client import ApiClient


class TestTicketingAttachmentResponse(unittest.TestCase):
    """TicketingAttachmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTicketingAttachmentResponse(self):
        """Test TicketingAttachmentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TicketingAttachmentResponse()  # noqa: E501

        """
        No test json responses were defined for TicketingAttachmentResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (TicketingAttachmentResponse,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.warnings is not None
        assert deserialized.errors is not None


if __name__ == '__main__':
    unittest.main()

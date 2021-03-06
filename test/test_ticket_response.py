"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import MergeTicketingClient
from MergeTicketingClient.model.debug_mode_log import DebugModeLog
from MergeTicketingClient.model.error_validation_problem import ErrorValidationProblem
from MergeTicketingClient.model.ticket import Ticket
from MergeTicketingClient.model.warning_validation_problem import WarningValidationProblem
globals()['DebugModeLog'] = DebugModeLog
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['Ticket'] = Ticket
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergeTicketingClient.model.ticket_response import TicketResponse


class TestTicketResponse(unittest.TestCase):
    """TicketResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTicketResponse(self):
        """Test TicketResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TicketResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

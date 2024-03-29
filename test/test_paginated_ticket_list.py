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
from MergeTicketingClient.model.ticket import Ticket
globals()['Ticket'] = Ticket
from MergeTicketingClient.model.paginated_ticket_list import PaginatedTicketList
from MergeTicketingClient.api_client import ApiClient


class TestPaginatedTicketList(unittest.TestCase):
    """PaginatedTicketList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedTicketList(self):
        """Test PaginatedTicketList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedTicketList()  # noqa: E501

        """
        No test json responses were defined for PaginatedTicketList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedTicketList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()

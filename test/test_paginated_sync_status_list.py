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
from MergeTicketingClient.model.sync_status import SyncStatus
globals()['SyncStatus'] = SyncStatus
from MergeTicketingClient.model.paginated_sync_status_list import PaginatedSyncStatusList
from MergeTicketingClient.api_client import ApiClient


class TestPaginatedSyncStatusList(unittest.TestCase):
    """PaginatedSyncStatusList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedSyncStatusList(self):
        """Test PaginatedSyncStatusList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedSyncStatusList()  # noqa: E501

        """
        No test json responses were defined for PaginatedSyncStatusList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedSyncStatusList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()

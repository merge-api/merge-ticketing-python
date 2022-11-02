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
from MergeTicketingClient.model.linked_account_condition_request import LinkedAccountConditionRequest
globals()['LinkedAccountConditionRequest'] = LinkedAccountConditionRequest
from MergeTicketingClient.model.linked_account_selective_sync_configuration_request import LinkedAccountSelectiveSyncConfigurationRequest
from MergeTicketingClient.api_client import ApiClient


class TestLinkedAccountSelectiveSyncConfigurationRequest(unittest.TestCase):
    """LinkedAccountSelectiveSyncConfigurationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLinkedAccountSelectiveSyncConfigurationRequest(self):
        """Test LinkedAccountSelectiveSyncConfigurationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LinkedAccountSelectiveSyncConfigurationRequest()  # noqa: E501

        """
        No test json responses were defined for LinkedAccountSelectiveSyncConfigurationRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (LinkedAccountSelectiveSyncConfigurationRequest,), False)

        assert deserialized is not None

        assert deserialized.linked_account_conditions is not None


if __name__ == '__main__':
    unittest.main()

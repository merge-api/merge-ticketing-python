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
from MergeTicketingClient.model.debug_model_log_summary import DebugModelLogSummary
from MergeTicketingClient.api_client import ApiClient


class TestDebugModelLogSummary(unittest.TestCase):
    """DebugModelLogSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDebugModelLogSummary(self):
        """Test DebugModelLogSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DebugModelLogSummary()  # noqa: E501

        raw_json = """
            {"url": "https://harvest.greenhouse.io/v1/candidates/", "method": "POST", "status_code": 200}
        """

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (DebugModelLogSummary,), False)

        assert deserialized is not None

        assert deserialized.url is not None
        assert deserialized.method is not None
        assert deserialized.status_code is not None


if __name__ == '__main__':
    unittest.main()

"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeTicketingClient
from MergeTicketingClient.api.account_token_api import AccountTokenApi  # noqa: E501


class TestAccountTokenApi(unittest.TestCase):
    """AccountTokenApi unit test stubs"""

    def setUp(self):
        self.api = AccountTokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_token_retrieve(self):
        """Test case for account_token_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()

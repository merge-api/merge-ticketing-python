"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeTicketingClient
from MergeTicketingClient.api.tickets_api import TicketsApi  # noqa: E501


class TestTicketsApi(unittest.TestCase):
    """TicketsApi unit test stubs"""

    def setUp(self):
        self.api = TicketsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tickets_collaborators_list(self):
        """Test case for tickets_collaborators_list

        """
        pass

    def test_tickets_create(self):
        """Test case for tickets_create

        """
        pass

    def test_tickets_list(self):
        """Test case for tickets_list

        """
        pass

    def test_tickets_meta_patch_retrieve(self):
        """Test case for tickets_meta_patch_retrieve

        """
        pass

    def test_tickets_meta_post_retrieve(self):
        """Test case for tickets_meta_post_retrieve

        """
        pass

    def test_tickets_partial_update(self):
        """Test case for tickets_partial_update

        """
        pass

    def test_tickets_retrieve(self):
        """Test case for tickets_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()

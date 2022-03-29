"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeTicketingClient
from MergeTicketingClient.api.attachments_api import AttachmentsApi  # noqa: E501


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = AttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attachments_create(self):
        """Test case for attachments_create

        """
        pass

    def test_attachments_list(self):
        """Test case for attachments_list

        """
        pass

    def test_attachments_meta_post_retrieve(self):
        """Test case for attachments_meta_post_retrieve

        """
        pass

    def test_attachments_retrieve(self):
        """Test case for attachments_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()

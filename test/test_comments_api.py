"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeTicketingClient
from MergeTicketingClient.api.comments_api import CommentsApi  # noqa: E501


class TestCommentsApi(unittest.TestCase):
    """CommentsApi unit test stubs"""

    def setUp(self):
        self.api = CommentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_comments_create(self):
        """Test case for comments_create

        """
        pass

    def test_comments_list(self):
        """Test case for comments_list

        """
        pass

    def test_comments_meta_post_retrieve(self):
        """Test case for comments_meta_post_retrieve

        """
        pass

    def test_comments_retrieve(self):
        """Test case for comments_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()

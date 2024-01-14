#!/usr/bin/python3
"""Test module for the review class"""

import unittest
from models.review import Review
from models.base_model import time_format
from datetime import datetime


class TestReview(unittest.TestCase):
    """Unit test for review"""

    def test_init_kwargs(self):
        """Test Initialization with arguments"""

        review_model1 = Review()
        review_dict = review_model1.to_dict()
        created_at = datetime.strptime(review_dict['created_at'], time_format)
        updated_at = datetime.strptime(review_dict['updated_at'], time_format)
        review_model2 = Review(**review_dict)

        self.assertEqual(review_model2.id, review_dict['id'])
        self.assertEqual(review_model2.created_at, created_at)
        self.assertEqual(review_model2.updated_at, updated_at)
        self.assertEqual(review_model2.place_id, "")
        self.assertEqual(review_model2.user_id, "")
        self.assertEqual(review_model2.text, "")

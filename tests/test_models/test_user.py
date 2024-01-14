#!/usr/bin/python3
"""Test module for the user class"""

import unittest
from models.user import User
from models.base_model import time_format
from datetime import datetime


class TestUser(unittest.TestCase):
    """Unit test for user"""

    def test_init_kwargs(self):
        """Test Initialization with arguments"""

        user_model1 = User()
        user_dict = user_model1.to_dict()
        created_at = datetime.strptime(user_dict['created_at'], time_format)
        updated_at = datetime.strptime(user_dict['updated_at'], time_format)
        user_model2 = User(**user_dict)

        self.assertEqual(user_model2.id, user_dict['id'])
        self.assertEqual(user_model2.created_at, created_at)
        self.assertEqual(user_model2.updated_at, updated_at)
        self.assertEqual(user_model2.email, "")
        self.assertEqual(user_model2.first_name, "")
        self.assertEqual(user_model2.last_name, "")
        self.assertEqual(user_model2.password, "")

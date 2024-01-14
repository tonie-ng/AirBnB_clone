#!/usr/bin/python3
"""Test module for the state class"""

import unittest
from models.state import State
from models.base_model import time_format
from datetime import datetime


class TestState(unittest.TestCase):
    """Unit test for state"""

    def test_init_kwargs(self):
        """Test Initialization with arguments"""

        state_model1 = State()
        state_dict = state_model1.to_dict()
        created_at = datetime.strptime(state_dict['created_at'], time_format)
        updated_at = datetime.strptime(state_dict['updated_at'], time_format)
        state_model2 = State(**state_dict)

        self.assertEqual(state_model2.id, state_dict['id'])
        self.assertEqual(state_model2.created_at, created_at)
        self.assertEqual(state_model2.updated_at, updated_at)
        self.assertEqual(state_model2.name, "")

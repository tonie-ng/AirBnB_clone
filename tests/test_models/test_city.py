#!/usr/bin/python3
"""Test module for the city class"""

import unittest
from models.city import City
from models.base_model import time_format
from datetime import datetime


class TestCity(unittest.TestCase):
    """Unit test for city"""

    def test_init_kwargs(self):
        """Test Initialization with arguments"""

        city_model1 = City()
        city_dict = city_model1.to_dict()
        created_at = datetime.strptime(city_dict['created_at'], time_format)
        updated_at = datetime.strptime(city_dict['updated_at'], time_format)
        city_model2 = City(**city_dict)

        self.assertEqual(city_model2.id, city_dict['id'])
        self.assertEqual(city_model2.created_at, created_at)
        self.assertEqual(city_model2.updated_at, updated_at)
        self.assertEqual(city_model2.name, "")
        self.assertEqual(city_model2.state_id, "")

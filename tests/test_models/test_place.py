#!/usr/bin/python3
"""Test module for the place class"""

import unittest
from models.place import Place
from models.base_model import time_format
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Unit test for place"""

    def test_init_kwargs(self):
        """Test Initialization with arguments"""

        place_model1 = Place()
        place_dict = place_model1.to_dict()
        created_at = datetime.strptime(place_dict['created_at'], time_format)
        updated_at = datetime.strptime(place_dict['updated_at'], time_format)
        place_model2 = Place(**place_dict)

        self.assertEqual(place_model2.id, place_dict['id'])
        self.assertEqual(place_model2.created_at, created_at)
        self.assertEqual(place_model2.updated_at, updated_at)
        self.assertEqual(place_model2.name, "")
        self.assertEqual(place_model2.city_id, "")
        self.assertEqual(place_model2.user_id, "")
        self.assertEqual(place_model2.description, "")
        self.assertEqual(place_model2.number_rooms, 0)
        self.assertEqual(place_model2.number_bathrooms, 0)
        self.assertEqual(place_model2.max_guest, 0)
        self.assertEqual(place_model2.price_by_night, 0)
        self.assertEqual(place_model2.longitude, 0.0)
        self.assertEqual(place_model2.latitude, 0.0)
        self.assertEqual(place_model2.amenity_ids, [])

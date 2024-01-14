#!/usr/bin/python3
"""Test module for the amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import time_format
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Unit test for amenity"""

    def test_init_kwargs(self):
        """Test Initialization with arguments"""

        amenity_model1 = Amenity()
        amenity_dict = amenity_model1.to_dict()
        created_at = datetime.strptime(amenity_dict['created_at'], time_format)
        updated_at = datetime.strptime(amenity_dict['updated_at'], time_format)
        amenity_model2 = Amenity(**amenity_dict)

        self.assertEqual(amenity_model2.id, amenity_dict['id'])
        self.assertEqual(amenity_model2.created_at, created_at)
        self.assertEqual(amenity_model2.updated_at, updated_at)
        self.assertEqual(amenity_model2.name, "")

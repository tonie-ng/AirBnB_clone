#!/usr/bin/python3
"""
Unit tests for Base Model
"""

import unittest
from models.base_model import BaseModel, time_format
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unit test for base model class."""

    def test_init(self):
        """Test Initialization"""

        base_model = BaseModel()

        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.updated_at)
        self.assertIsNotNone(base_model.created_at)

    def test_init_kwargs(self):
        """Test Initialization with arguments"""

        base_model1 = BaseModel()
        base_model1.name = "Test model"
        base_model1.number = 12
        base_dict = base_model1.to_dict()
        created_at = datetime.strptime(base_dict['created_at'], time_format)
        updated_at = datetime.strptime(base_dict['updated_at'], time_format)
        base_model2 = BaseModel(**base_dict)

        self.assertEqual(base_model2.id, base_dict['id'])
        self.assertEqual(base_model2.created_at, created_at)
        self.assertEqual(base_model2.updated_at, updated_at)
        self.assertEqual(base_model2.number, 12)
        self.assertEqual(base_model2.name, "Test model")

    def test_uniqueid(self):
        """Test for Unique ID"""

        base_model1 = BaseModel()
        base_model2 = BaseModel()
        base_model3 = BaseModel()

        self.assertNotEqual(base_model1.id, base_model2.id, base_model3)

    def test_save(self):
        """Test save method"""

        base_model = BaseModel()
        updated_at = base_model.updated_at
        base_model.save()

        self.assertNotEqual(updated_at, base_model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""

        base_model = BaseModel()
        base_dict = base_model.to_dict()
        created_at = base_model.created_at.isoformat()
        updated_at = base_model.updated_at.isoformat()

        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(base_dict['id'], base_model.id)
        self.assertEqual(base_dict['created_at'], created_at)
        self.assertEqual(base_dict['updated_at'], updated_at)

    def test__str(self):
        """Test __str__ method"""

        base_model = BaseModel()
        name = base_model.__class__.__name__
        base_dict = base_model.__dict__

        self.assertIsInstance(str(base_model), str)
        self.assertIn(base_model.id, str(base_model))
        self.assertIn(name, str(base_model))
        self.assertIn(str(base_dict), str(base_model))

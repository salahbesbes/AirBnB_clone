#!/usr/bin/python3
"""
    Test Case For city Model and its Test
"""
from models import BaseModel
from models import City
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
from unittest import mock
import models


class TestCity(unittest.TestCase):
    """
        unitesst for City class
    """
    def issub_class(self):
        """
            test if City class is sub class of base model
        """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "update_at"))

    def test_class_attribute(self):
        """
            test for class attribute
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_to_dictcity(self):
        """
            test to dict method with city and the type
            and content
        """
        city = City()
        dict_cont = city.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in city.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        dict_con = city.to_dict()
        self.assertEqual(dict_con["__class__"], "City")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
                            dict_con["created_at"],
                            city.created_at.strftime(time_format)
                                        )
        self.assertEqual(
                            dict_con["updated_at"],
                            city.updated_at.strftime(time_format))

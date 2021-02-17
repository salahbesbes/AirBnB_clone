#!/usr/bin/python3
"""
    Test Case For Amenity Model and its Test
"""
from models import BaseModel
from models import Amenity
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
from unittest import mock
import models


class TestAmenity(unittest.TestCase):
    """
        unitesst for user class
    """
    def issub_class(self):
        """
            test if Amenity class is sub class of base model
        """
        insta = Amenity()
        self.assertIsInstance(insta, BaseModel)
        self.assertTrue(hasattr(insta, "id"))
        self.assertTrue(hasattr(insta, "created_at"))
        self.assertTrue(hasattr(insta, "update_at"))

    def test_name(self):
        """
            test class atribute name
        """
        insta = Amenity()
        self.assertTrue(hasattr(insta, "name"))
        self.assertEqual(insta.name, "")

    def test_to_dictAmenity(self):
        """
            test to dict method with Amenity and the type
            and content
        """
        insta = Amenity()
        dict_cont = insta.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in insta.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        insta = Amenity()
        dict_con = insta.to_dict()
        self.assertEqual(dict_con["__class__"], "Amenity")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
                            dict_con["created_at"],
                            insta.created_at.strftime(time_format)
                                        )
        self.assertEqual(
                            dict_con["updated_at"],
                            insta.updated_at.strftime(time_format))

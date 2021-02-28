#!/usr/bin/python3
"""
    Test Case For Place Model and its Test
"""
from models import BaseModel
from models import Place
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
from unittest import mock
import models


class TestPlace(unittest.TestCase):
    """
        unitesst for Place class
    """
    def issub_class(self):
        """
            test if Place class is sub class of base model
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "update_at"))

    def test_city_id_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_description_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_latitude_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dictPlace(self):
        """
            test to dict method with Place and the type
            and content
        """
        place = Place()
        dict_cont = place.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in place.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        dict_con = place.to_dict()
        self.assertEqual(dict_con["__class__"], "Place")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
                            dict_con["created_at"],
                            place.created_at.strftime(time_format)
                                        )
        self.assertEqual(
                            dict_con["updated_at"],
                            place.updated_at.strftime(time_format))

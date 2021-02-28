#!/usr/bin/python3
"""
    Test Case For Review Model and its Test
"""
from models import BaseModel
from models import Review
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
from unittest import mock
import models


class TestReview(unittest.TestCase):
    """
        unitesst for Review class
    """
    def issub_class(self):
        """
            test if Review class is sub class of base model
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "update_at"))

    def test_place_id_attr(self):
        """
            test for class attribute
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """
            test for class attribute
        """
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """
            test for class attribute
        """
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_to_dictReview(self):
        """
            test to dict method with Review and the type
            and content
        """
        review = Review()
        dict_cont = review.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in review.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        review = Review()
        dict_con = review.to_dict()
        self.assertEqual(dict_con["__class__"], "Review")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
                            dict_con["created_at"],
                            review.created_at.strftime(time_format)
                                        )
        self.assertEqual(
                            dict_con["updated_at"],
                            review.updated_at.strftime(time_format))

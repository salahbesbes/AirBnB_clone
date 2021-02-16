#!usr/bin/python3
"""
    Unittest for Base Module
"""
import pycodestyle
import inspect
import unittest
from models import base_model
import models
import glob

Base = base_model.BaseModel


class TestCodeFormat(unittest.TestCase):

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide()
        # because the test is running from this current directory
        style.input_dir('../../')
        style.input_dir('.')
        result = style.check_files()
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """
            Check base module Docstring
        """
        print("------- Testing Doc Base Module -------")
        files = []

        print(glob.glob("/home/salah_besbes/salah/AirBnB_clone/*.py"))
        self.assertTrue(len(base_model.__doc__) >= 1)

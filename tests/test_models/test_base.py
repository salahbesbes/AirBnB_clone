#!usr/bin/python3
"""
    Unittest for Base Module
"""
import pep8
import inspect
import unittest
from models import base_model
Base = base_model.BaseModel


class TestDocBase(unittest.TestCase):
    """
        Testing Documentaion and Pep8 for The Base Module
    """
    @classmethod
    def SetUpClass(cls):
        """
            Set up For Documentaion and pep8 tests
        """
        cls.base_module_func = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8(self):
        """
            Check pep8 for base module file
        """
        pep = pep8.StyleGuide(quiet=True)
        result = pep.check_files(['models/base_model.py'])
        self.assertEqual(
                        result.total_errors, 0,
                        "Found Code style and warning")

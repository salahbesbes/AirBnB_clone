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
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_base_module(self):
        """
            Check pep8 for base module file
        """
        print("------- Testing Pep8 Base Module -------")
        pep = pep8.StyleGuide(quiet=True)
        res = pep.check_files(['models/base_model.py'])
        self.assertEqual(
            res.total_errors, 0,
            "Found Code style and warning")

    def test_pep8_for_test_base_module(self):
        """
            Check pep8 for your unitesst for base module
        """
        print("------ Testing pep8 for Test base module -------")
        pep = pep8.StyleGuide(quiet=True)
        res = pep.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(
            res.total_errors, 0,
            "Found Code style and warning")

    def test_base_docstring(self):
        """
            Check base module Docstring
        """
        print("------- Testing Doc Base Module -------")
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_doc(self):
        """
            Testing Class Docstring
        """
        print("------- Testing Doc Class Base Module -------")
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_doc(self):
        """
            Testing All function inside base module class
        """
        print("-------- Testing Func Doc -----------")
        print("To Do")

    class TestBaseModule(unittest.TestCase):
        """
            Test For Base Module
        """

        def test_module_args(self):
            """
                Testing Module Args
            """
            print("------ Testing module with Args -------")
            with self.assertRaises(TypeError):
                a = Base(1, 1)
                b = Base(2)
                g = Base(1, 2, 3, 4)

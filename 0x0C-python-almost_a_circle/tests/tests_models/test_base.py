#!/usr/bin/python3
"""This module defines the unit test cases for base class"""
import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """This class represents unittest for testing instantiation
        of the base class
    """

    def test_no_args(self):
        """This function test for no arg passed"""

        b1 = Base()
        b2 = Base()

        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """Test case for three bases instances"""

        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """This test case test for none id passed"""

        b1 = Base(None)
        b2 = Base(None)

        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """Test case for unique id passed"""

        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_nb_instance_after_uniq_id(self):
        """Test case checks that the Base class assigns unique
            IDs properly
        """

        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_public_id(self):
        """Test case for public ids"""

        b = Base(42)
        b.id = 12
        self.assertEqual(12, b.id)

    def test_string_id(self):
        """Test case for string ids"""
        b = Base("python")
        self.assertEqual(b.id, "python")

    def test_float_id(self):
        """Test case for float ids"""

        b = Base(2.3)
        self.assertEqual(b.id, 2.3)

    def test_complex_id(self):
        """Test case for complex id"""

        b = Base(complex(4))
        self.assertEqual(b.id, complex(4))

    def test_bool_id(self):
        """Test case for bool id"""

        b = Base(True)
        self.assertEqual(b.id, True)

    def test_dict_id(self):
        """Test case for the dictionary id"""

        b = Base({"x": 2, "y": 4})
        self.assertEqual(b.id, {"x": 2, "y": 4})

    def test_tuple_id(self):
        """Test case for tuple id"""

        b = Base((1, 3))
        self.assertEqual(b.id, (1, 3))

    def test_set_id(self):
        """Test case for set ids"""

        b = Base({1, 2, 3, 4})
        self.assertEqual(b.id, {1, 2, 3, 4})

    def test_frozenset_id(self):
        """Test for frozenset id"""

        b = Base(frozenset({1, 2, 3}))
        self.assertEqual(b.id, frozenset({1, 2, 3}))

    def test_range_id(self):
        """Test case for range id"""

        b = Base(range(6))
        self.assertEqual(b.id, range(6))

    def test_infinit_id(self):
        """Test for infinte id"""

        b = Base(float('inf'))
        self.assertEqual(b.id, float('inf'))

    def test_two_args(self):
        """Test case that checks for two arguments"""

        with self.assertRaises(TypeError):
            Base(2, 3)


if __name__ == '__main__':
    unittest.main()

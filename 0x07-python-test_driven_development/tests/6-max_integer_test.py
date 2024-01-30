#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define the unittest"""

    def test_empty_list(self):
        """Test for an empty list"""

        result = max_integer([])
        self.assertIsNone(result)

    def test_ordered_list(self):
        """Test for the ordered list"""

        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test for unordered list"""

        unordered = [1, 3, 2, 4]
        self.assertEqual(max_integer(unordered), 4)

    def test_at_beginning(self):
        """TEst a list with a beginning max value"""

        max_begining = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_begining), 4)

    def test_one_element_list(self):
        """Test for on element in the list"""

        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats_in_list(self):
        """Test a list with float values"""

        list_floats = [1.45, 2.34, 7.07, 10.4]
        self.assertEqual(max_integer(list_floats), 10.4)

    def test_int_float(self):
        """Test both floats and integers in a list"""

        int_float = [-8, 1.23, 5, 7.8]
        self.assertEqual(max_integer(int_float), 7.8)

    def test_string(self):
        """Test a list of string"""

        string = "John"
        self.assertEqual(max_integer(string), 'o')

    def test_list_strings(self):
        """Test a list of string"""

        list_string = ["John", "is", "my", "name"]
        self.assertEqual(max_integer(list_string), "name")

    def empty_string(self):
        """Test for an empty string"""

        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()

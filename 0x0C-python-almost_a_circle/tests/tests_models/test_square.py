#!/usr/bin/python3
"""This module define a test case for class square"""
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """This class represents the test cases for Square
        instantiations
    """

    def test_square_is_base(self):
        """Test that checks if a Square isinstance of a base"""

        s = Square(12, 3)
        self.assertIsInstance(s, Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(12)
        s2 = Square(2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(1, 2)
        s2 = Square(3, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(2, 2, 3)
        s2 = Square(3, 3, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, 4)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)

    def test_private_size(self):
        with self.assertRaises(AttributeError):
            print(Square(4, 4, 5, 3).__size)

    def test_size_getter(self):
        s = Square(4, 5, 5, 4)
        self.assertEqual(s.size, 4)

    def test_size_setter(self):
        s = Square(4, 5, 5, 4)
        s.size = 7
        self.assertEqual(s.size, 7)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Square(4, 4, 0, 3).__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Square(4, 4, 0, 3).__y)

    def test_width_getter(self):
        s = Square(4, 5, 5, 4)
        self.assertEqual(s.width, 4)

    def test_width_setter(self):
        s = Square(5, 5, 4, 1)
        s.width = 7
        self.assertEqual(s.width, 7)

    def test_x_getter(self):
        s = Square(4, 5, 5, 4)
        self.assertEqual(s.x, 5)

    def test_x_setter(self):
        s = Square(5, 5, 4, 1)
        s.x = 6
        self.assertEqual(s.x, 6)

    def test_y_getter(self):
        s = Square(4, 5, 5, 4)
        self.assertEqual(s.y, 5)

    def test_y_setter(self):
        s = Square(4, 5, 5, 4)
        s.y = 7
        self.assertEqual(s.y, 7)


class TestSquareSize(unittest.TestCase):
    """this class test for initiaization of Square size"""

    def test_None_size(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.4, 4)

    def test_string_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("4", 7)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(4), 5)

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"x": 4, "y": 6}, 9)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 7)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 3), 2)

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3, 4}, 7)

    def test_frozen_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3}), 6)

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(7), 5)

    def test_infinite_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 4, 5, 7)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3, 5, 6)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 3, 4)


class TestSquare_x(unittest.TestCase):
    """This class represents unittest for initializing
        x attribute
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "3", 4)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, complex(4), 5, 8)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {"x": 4, "y": 6})

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, [1, 2, 3])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, (1, 3))

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, {1, 2, 3, 4})

    def test_frozen_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, frozenset({1, 2, 3}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, range(7))

    def test_infinite_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, float('inf'))

    def test_zero_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -6)


class TestSquare_y(unittest.TestCase):
    """unittests for testing initialization of Rectangle x attribute"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, None, 4)

    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 3, "4")

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, complex(4))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, {"x": 4, "y": 6})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 3, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 5, (1, 3))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 6, {1, 2, 3, 4})

    def test_frozen_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(6, 8, frozenset({1, 2, 3}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 7, range(7))

    def test_infinite_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 4, float('inf'))

    def test_zero_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 4, -6)


if __name__ == '__main__':
    unittest.main()

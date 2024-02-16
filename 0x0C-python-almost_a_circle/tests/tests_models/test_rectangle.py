#!/usr/bin/python3
"""This module define a test case for class rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """This class represents the test cases for recatangle
        instantiations
    """

    def test_rectangle_is_base(self):
        """Test that checks if a rectangle isinstance of a base"""

        r = Rectangle(12, 3)
        self.assertIsInstance(r, Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 3)
        r2 = Rectangle(3, 3, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(Rectangle(10, 3, 0, 0, 12).id, 12)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 3).__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 3).__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 3).__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 3).__y)

    def test_width_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.width, 4)

    def test_width_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_height_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.height, 5)

    def test_height_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.height = 7
        self.assertEqual(r.height, 7)

    def test_x_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.x, 5)

    def test_x_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.x = 7
        self.assertEqual(r.x, 7)

    def test_y_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.y, 4)

    def test_y_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.y = 7
        self.assertEqual(r.y, 7)


class TestRectangleWidth(unittest.TestCase):
    """this class test for initiaization of rectangle width"""

    def test_None_width(self):
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.4, 3)

    def test_string_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("4", 4)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 4)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"x": 4, "y": 6}, 6)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 7)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 3), 3)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3, 4}, 5)

    def test_frozen_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 5)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(7), 5)

    def test_infinite_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 4)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 6)


class TestRectangleHeight(unittest.TestCase):
    """This class represent testing initialization for
        height attribute of the rectangle
    """

    def test_None_height(self):
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 3.4)

    def test_string_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "4")

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, complex(4))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {"x": 4, "y": 6})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [1, 2, 3])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (1, 3))

    def test_set_heigh(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {1, 2, 3, 4})

    def test_frozen_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, frozenset({1, 2, 3}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, range(7))

    def test_infinite_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -4)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0)


class TestRectangle_x(unittest.TestCase):
    """This class represents unittest for initializing
        x attribute
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, None)

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, "3", 4)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, complex(4))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, {"x": 4, "y": 6})

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, [1, 2, 3])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, (1, 3))

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 6, {1, 2, 3, 4})

    def test_frozen_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 8, frozenset({1, 2, 3}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 7, range(7))

    def test_infinite_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, float('inf'))

    def test_zero_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -6)


class TestRectangle_y(unittest.TestCase):
    """unittests for testing initialization of Rectangle x attribute"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 3, None)

    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 3, "4")

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, complex(4))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 5, {"x": 4, "y": 6})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 3, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 5, (1, 3))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 6, 6, {1, 2, 3, 4})

    def test_frozen_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 8, 8, frozenset({1, 2, 3}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 7, 7, range(7))

    def test_infinite_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 4, float('inf'))

    def test_zero_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 6, -6)


class TestRectangleArea(unittest.TestCase):
    """This unittest tests for area of the rectangle"""

    def test_small_area(self):
        r = Rectangle(12, 3, 0, 0, 7)
        self.assertEqual(r.area(), 36)

    def test_large_area(self):
        r = Rectangle(999999, 999999, 0, 0, 4)
        self.assertEqual(r.area(), 999998000001)

    def test_changed_attribute(self):
        r = Rectangle(4, 7, 2, 2, 6)
        r.width = 8
        r.height = 10
        self.assertEqual(r.area(), 80)

    def test_one_arg(self):
        r = Rectangle(10, 23, 0, 0, 4)
        with self.assertRaises(TypeError):
            r.area(3)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()

import unittest
import os
import io
import sys

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Reset Base class instance count before each test"""
        Base._Base__nb_objects = 0

    def test_instance_class(self):
        """Checks for a instance of the class
        """
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))
        r2 = Rectangle(2, 5)
        self.assertTrue(type(r1) == type(r2))
        self.assertFalse(id(r1) == id(r2))

    def test_area(self):
        """Check area method of rectangle objects
        """
        r1 = Rectangle(3, 2)
        area = r1.area()
        self.assertEqual(area, 6)

        r2 = Rectangle(3, 2)
        area = Rectangle.area(r2)
        self.assertEqual(area, 6)

        r3 = Rectangle(30, 20, 4, 5, 10)
        area = r3.area()
        self.assertEqual(area, 600)

        r4 = Rectangle(5, 5, 4)
        area = r4.area()
        self.assertEqual(area, 25)

    def test_rectangle_instance_count(self):
        """Test instance count"""
        rectangle_count = Base._Base__nb_objects
        r1 = Rectangle(4, 5)
        r2 = Rectangle(2, 3)
        self.assertEqual(Base._Base__nb_objects, rectangle_count + 2)

    def test_rectangle_id(self):
        """Test ID assignment"""
        r1 = Rectangle(4, 5)
        r2 = Rectangle(2, 3, 1, 1, 10)
        r3 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 10)
        self.assertEqual(r3.id, 2)

    def test_rectangle_width(self):
        """Test width attribute"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.width, 4)
        r1.width = 10
        self.assertEqual(r1.width, 10)
        with self.assertRaises(ValueError):
            r1.width = -5

    def test_rectangle_height(self):
        """Test height attribute"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.height, 5)
        r1.height = 8
        self.assertEqual(r1.height, 8)
        with self.assertRaises(ValueError):
            r1.height = -3

    def test_rectangle_x(self):
        """Test x attribute"""
        r1 = Rectangle(4, 5, 2)
        self.assertEqual(r1.x, 2)
        r1.x = 6
        self.assertEqual(r1.x, 6)
        with self.assertRaises(ValueError):
            r1.x = -1

    def test_rectangle_y(self):
        """Test y attribute"""
        r1 = Rectangle(4, 5, 2, 3)
        self.assertEqual(r1.y, 3)
        r1.y = 7
        self.assertEqual(r1.y, 7)
        with self.assertRaises(ValueError):
            r1.y = -2

    def test_rectangle_area(self):
        """Test area method"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(3, 6)
        self.assertEqual(r2.area(), 18)

    def test_rectangle_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(4, 5, 2, 3)
        expected_dict = {'id': 1, 'width': 4, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(r1.to_dictionary(), expected_dict)

    def test_rectangle_str(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 5, 2, 3)
        expected_str = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(str(r1), expected_str)

    def test_rectangle_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(4, 5, 2, 3)
        r2 = Rectangle(2, 3, 1, 1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            file_contents = file.read()
            self.assertIn(str(r1.id), file_contents)
            self.assertIn(str(r2.id), file_contents)

    def test_rectangle_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(4, 5, 2, 3)
        r2 = Rectangle(2, 3, 1, 1)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)
        self.assertEqual(rectangles[0].id, r1.id)
        self.assertEqual(rectangles[1].id, r2.id)
        self.assertEqual(rectangles[0].width, r1.width)
        self.assertEqual(rectangles[1].width, r2.width)
        self.assertEqual(rectangles[0].height, r1.height)
        self.assertEqual(rectangles[1].height, r2.height)
        self.assertEqual(rectangles[0].x, r1.x)
        self.assertEqual(rectangles[1].x, r2.x)
        self.assertEqual(rectangles[0].y, r1.y)
        self.assertEqual(rectangles[1].y, r2.y)


if __name__ == "__main__":
    unittest.main()

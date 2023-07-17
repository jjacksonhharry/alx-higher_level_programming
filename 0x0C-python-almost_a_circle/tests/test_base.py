import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset Base class instance count before each test"""
        Base._Base__nb_objects = 0

    def test_base_instance_count(self):
        """Test instance count"""
        base_count = Base._Base__nb_objects
        b1 = Base()
        b2 = Base()
        self.assertEqual(Base._Base__nb_objects, base_count + 2)

    def test_instance_type_id_class(self):
        """Checks for a instance of the class
        """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b2 = Base()
        self.assertTrue(type(b1) == type(b2))
        self.assertFalse(id(b1) == id(b2))

    def test_none_id(self):
        """Checks when id is none
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 4)

    def test_id_value(self):
        """Checks when id has a integer value
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1.id = 4
        self.assertEqual(b1.id, 4)
        b2 = Base(50)
        self.assertEqual(b2.id, 50)
        b1 = Base(-4)
        self.assertEqual(b1.id, -4)
        b2 = Base(0)
        self.assertEqual(b2.id, 0)
        b1 = Base(100e+1000)
        self.assertEqual(b1.id, 100e+1000)
        b1.__init__(30)
        self.assertEqual(b1.id, 30)

    def test_base_id(self):
        """Test ID assignment"""
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)
        self.assertEqual(b4.id, 3)

    def test_base_from_json_string(self):
        """Test from_json_string method"""
        json_string = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(type(list_dicts), list)
        self.assertEqual(list_dicts, [{'x': 2, 'y': 8, 'id': 1, 'width': 10, 'height': 7}])

    def test_base_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 3)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_base_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 3)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertTrue(all(isinstance(rect, Rectangle) for rect in rectangles))

    def test_square_save_to_file(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            result = f.read()
            self.assertEqual(result, '[]')

    def tearDown(self):
        """Remove created files after each test"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()

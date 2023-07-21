import unittest
import os

from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    def setUp(self):
        """Reset Base class instance count before each test"""
        Base._Base__nb_objects = 0

    def test_square_instance_count(self):
        """Test instance count"""
        square_count = Base._Base__nb_objects
        s1 = Square(5)
        s2 = Square(3)
        self.assertEqual(Base._Base__nb_objects, square_count + 2)

    def test_square_id(self):
        """Test ID assignment"""
        s1 = Square(5)
        s2 = Square(3, 4)
        s3 = Square(2, 1, 1, 10)
        s4 = Square(1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 10)
        self.assertEqual(s4.id, 3)

    def test_square_size(self):
        """Test size attribute"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        with self.assertRaises(ValueError):
            s1.size = -5

    def test_invalid_args(self):
        """Check if the Square constructor handles invalid arguments"""
        with self.assertRaises(ValueError):
            """Negative size"""
            s = Square(-1)

        with self.assertRaises(ValueError):
            """Zero size"""
            s = Square(0)

    def test_invalid_type_args(self):
        """Check if the Square constructor handles invalid type arguments"""
        with self.assertRaises(TypeError):
            """Size as a string"""
            s = Square("1")

        with self.assertRaises(TypeError):
            """x coordinate as a string"""
            s = Square(1, "2")

        with self.assertRaises(TypeError):
            """y coordinate as a string"""
            s = Square(1, 2, "3")

        with self.assertRaises(TypeError):
            """Size as a float"""
            s = Square(1.5)

        with self.assertRaises(TypeError):
            """x coordinate as a float"""
            s = Square(1, 2.5)

        with self.assertRaises(TypeError):
            """y coordinate as a float"""
            s = Square(1, 2, 3.5)

    def test_square_area(self):
        """Test area method"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(3)
        self.assertEqual(s2.area(), 9)

    def test_str(self):
        """Check str method"""
        s1 = Square(4, 6, 2, 1)
        self.assertEqual(str(s1), "[Square] (1) 6/2 - 4")
        s2 = Square(5, 5, 1)
        self.assertEqual(str(s2), "[Square] (1) 5/1 - 5")
        s3 = Square(5, 5)
        self.assertEqual(str(s3), "[Square] (2) 5/0 - 5")
        s4 = Square(4, 6, 2, 50)
        self.assertEqual(s4.__str__(), "[Square] (50) 6/2 - 4")

    def test_square_update(self):
        """Test update method"""
        s1 = Square(5)
        s1.update(10, 7, 2, 8)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 8)

    def test_square_to_dictionary(self):
        """Test to_dictionary method"""
        s1 = Square(5, 2, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected_dict)

    def test_create(self):
        """Test the create method"""
        square_dict = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s = Square.create(**square_dict)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file(self):
        """Test the save_to_file method"""
        """Save an empty list of Square objects"""
        Square.save_to_file([])

        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))

        """Read the content of the file"""
        with open(filename, "r") as file:
            content = file.read()

        """Verify if the content is an empty list JSON representation"""
        self.assertEqual(content, "[]")

        """Remove the file after the test"""
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()

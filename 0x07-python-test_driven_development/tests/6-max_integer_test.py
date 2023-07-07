#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_intege"""

    def test_max_at_the_end(self):
        """ Test with the maximum value at the end of the list """
        result = max_integer([5, 2, 5, 9, 5])
        self.assertEqual(result, 9)

    def test_max_at_the_beginning(self):
        """ Test with the maximum value at the beginning of the list """
        result = max_integer([5, 4, 3, 2, 1])
        self.assertEqual(result, 5)

    def test_max_in_the_middle(self):
        """ Test with the maximum value in the middle of the list """
        result = max_integer([1, 2, 5, 3, 4])
        self.assertEqual(result, 5)

    def test_one_negative_number(self):
        """ Test with a list containing only one negative number """
        result = max_integer([-10])
        self.assertEqual(result, -10)

    def test_only_negative_numbers(self):
        """ Test with a list containing only negative numbers """
        result = max_integer([-5, -10, -2, -1])
        self.assertEqual(result, -1)

    def test_empty_list(self):
        """ Test with an empty list """
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """ Test with a list containing a single element """
        result = max_integer([5])
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

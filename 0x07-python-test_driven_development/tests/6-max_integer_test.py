#!/usr/bin/python3

"""
Unittest module to find max integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
    unittest class to find max int
    """

    def test_empty_list(self):

        """Validate that list isn't empty"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):

        """Evaluate list with one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_two_elements(self):

        """Evaluate list with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)

    def test_multiple_elements(self):

        """Evaluate list with multiple elements"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)


if __name__ == '__main__':
    unittest.main()

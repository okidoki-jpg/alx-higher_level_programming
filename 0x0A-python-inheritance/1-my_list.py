#!/usr/bin/python3
"""
MyList Class Module

Attributes:
    list (onject): list object
"""


class MyList(list):
    """
    class doc.

    Methods:
        print_sorted: print inherited list in asscending order
    """

    def print_sorted(self):
        """
        method doc: print sorted list
        """

        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)

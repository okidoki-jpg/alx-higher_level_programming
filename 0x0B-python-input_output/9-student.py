#!/usr/bin/python3

"""
Class Module Doc:

Methods:
    to_json - gets obj dictionary representation
"""


class Student:
    """
    Class Doc: Define Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Methid Dox: instantiate class
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        get obj dict representation
        """

        return self.__dict__

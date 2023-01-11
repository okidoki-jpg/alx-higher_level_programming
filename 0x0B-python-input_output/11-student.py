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

    def to_json(self, attrs=None):
        """
        get obj dict representation
        """

        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json)
    """
    clears/resets a student instance
    """

    for key, value in json.items():
        setattr(self, key, value)

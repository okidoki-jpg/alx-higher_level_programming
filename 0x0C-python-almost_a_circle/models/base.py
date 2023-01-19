#!/usr/bin/python3
"""
Class Module Doc: Base Class
"""


import json


class Base:
    """
    Class Doc: Base class definition

    Attributes:
    __nb_objects (int): private object counter attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Method Doc: Initialize class.

        Attributes:
            id (int): init id value
        """

        self.id = id

        if not id:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Attributes:
            list_dictionaries (list): A list of dictionaries

        Return:
            JSON string representation of 'list_dictionaries'
        """

        dicts = list_dictionaries
        if not dicts or len(dicts) == 0:
            return "[]"
        return json.dumps(dicts)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string representation of list_objs to a file

        Attributes:
            list_objs (list): A list of Base derived objects
        """

        dicts = []
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            if list_objs is not None:
                [dicts.append(i.to_dictionary()) for i in list_objs]
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Attributes:
            json_string (str): A string representing a list of
            dictionaries

        Return:
            A List of the JSON string representation
            `json_string`
        """

        if not json_string or not len(json_string):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Attributes:
            dictionary (**kwargs): kwargs to create objects

        Return:
            An instance with all attributes already set
        """

        new = cls(10, 8)
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        elif cls.__name__ == 'Square':
            new = cls(1)

        if new:
            new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Return:
            A list of instances
        """

        try:
            with open(f"{cls.__name__}.json", "r") as f:
                dicts = Base.from_json_string(f.read())
            return [cls.create(**dict_) for dict_ in dicts]
        except IOError:
            return []

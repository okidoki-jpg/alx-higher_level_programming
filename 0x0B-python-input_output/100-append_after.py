#!/usr/bin/python3
"""
Module Doc: add new text after line with specific string

Attributes:
    filename (str): path to file
    search_string (str): string delimeter
    new_string (str): new string to add
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function Doc: add new text after line with specific string
    """

    file = ""
    with open(filename, "r") as f:
        for line in f:
            file += line
            if search_string in line:
                file += new_string

    with open(filename, "w") as f:
        f.write(file)

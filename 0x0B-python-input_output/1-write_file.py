#!/usr/bin/python3
"""
Module Doc: Write a string to UTF-8 format text file

Attributes:
    filename (str): path to file
    text (str)    : string to write

Return:
    number of bytes written
"""


def write_file(filename="", text=""):
    """
    Function Doc: Write to a text file
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

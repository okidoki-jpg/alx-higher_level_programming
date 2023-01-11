#!/usr/bin/python3
"""
Module Doc: Apoend string to UTF-8 format text file

Attributes:
    filename (str): path to file
    text (str)    : string to append

Return:
    number of bytes written
"""


def append_write(filename="", text=""):
    """
    Function Doc: Append string to text file
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

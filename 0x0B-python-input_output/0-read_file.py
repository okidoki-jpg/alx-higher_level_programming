#!/usr/bin/python3
"""
Module Doc: read UTF-8 format text file

Attributes:
    filename (str): path to textfile
"""


def read_file(filename=""):
    """
    Funtion Doc: Read Text file
    """

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())

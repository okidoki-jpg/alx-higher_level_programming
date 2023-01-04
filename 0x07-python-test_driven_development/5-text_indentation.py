#!/usr/bin/python3

"""
Print a text with 2 new lines after each of these characters: ., ? and :

Attributes:
    text (string): text to print
"""


def text_indentation(text):

    """
    Validate that var 'text' is type string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """
    Print text characters
    """

    indent = False
    for c in text:
        if c in ".?:":
            print(c)
            print()
            indent = True
        elif c == " " and indent:
            continue
        else:
            print(c, end="")
            indent = False

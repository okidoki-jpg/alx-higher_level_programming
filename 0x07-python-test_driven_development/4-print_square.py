#!/usr/bin/python3

"""
Print a square with the character `#`

Attributes:
    size (int): dimension of the square
"""


def print_square(size):

    """
    Validate that 'size' is an int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    """
    Validate square dimension is >= 0
    """
    if size < 0:
        raise ValueError("size must be >= 0")

    print('\n'.join(["#" * size] * size))

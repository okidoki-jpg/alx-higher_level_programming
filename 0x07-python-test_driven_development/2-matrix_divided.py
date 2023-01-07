#!/usr/bin/python3

"""
A function dividing all elements of a matrix

Attributes:
    matrix (2d list): list with elements to divide
    div (int)       : value to divide elements by

Returns:
    new matrix with elements divided by div value
"""


def matrix_divided(matrix, div):

    """
    check that all elements are lists
    """
    if not all(isinstance(row, list) for row in matrix) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    """
    validate that matrix elments are type floatr/int
    """
    if not all((type(elem) in (int, float)) for row in matrix
               for elem in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    """
    validate that matrix rows are the same length
    """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """
    validate that div variable is type int/float
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """
    Validate that div variable is not '0'
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

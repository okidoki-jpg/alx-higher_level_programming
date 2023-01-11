#!/usr/bin/python3
"""
Moduke Doc: print pascal triangle
"""


def pascal_triangle(n):
    """
    Fubction Doc: print n sized pascal triqngle

    Attributes:
        n (int): size of triangle
    """

    result = []
    if n <= 0:
        return result

    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i-1][j-1] + result[i-1][j])
        result.append(row)
    return result

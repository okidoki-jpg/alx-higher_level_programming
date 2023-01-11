#!/usr/bin/python3
"""
Class Module Doc: invert eq & ne behavior

Attributes:
    int (object): base clasd
"""


class MyInt(int):
    """
    Class Doc: invert eq & ne behavior
    """

    def __eq__(self, other):
        """
        invert eq behavior
        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
        invert ne behavior
        """
        return super().__eq__(other)

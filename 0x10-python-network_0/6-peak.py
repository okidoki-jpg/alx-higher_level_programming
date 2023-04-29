#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    size = len(list_of_integers)
    if size <= 2:
        return max(list_of_integers)

	start = 0
    end = size - 1

    while start <= end:
        mid = (start + end) // 2
        peak = list_of_integers[mid]

        if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
            return peak
        elif peak < list_of_integers[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1

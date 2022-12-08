#!/usr/bin/python3
def best_score(a_dictionary):

    max_val = 0
    max_key = None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > max_val:
                max_val = v
                max_key = k
    return max_key

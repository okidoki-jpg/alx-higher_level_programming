#!/usr/bin/python3
def element_at(my_list, idx):

    if idx > -1 and (idx < len(my_list) or idx == 0):
        return my_list[idx]
    return None

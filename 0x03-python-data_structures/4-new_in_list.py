#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    new_list = my_list.copy()
    if idx > -1 and (idx < len(my_list) or idx == 0):
        new_list[idx] = element
    return new_list

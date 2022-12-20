#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        if my_list[x]:
            [print(i, end="") for i in my_list[:x]]
            print()
            return x
    except IndexError:
        idx = 0
        for i in my_list:
            print(i, end="")
            idx += 1
        print()
        return (idx)

#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    res, dist = [], abs(len(my_list_1) - len(my_list_2))
    try:
        for i, j in zip(my_list_1, my_list_2):
            try:
                res.append(i / j)
            except (TypeError, ValueError):
                print("wrong type")
                res.append(0)
            except ZeroDivisionError:
                print("division by 0")
                res.append(0)
        if dist > 0:
            print("out of range")
            res.extend([0 for i in range(list_length - len(res))])
    finally:
        return res

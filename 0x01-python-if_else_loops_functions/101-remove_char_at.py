#!/usr/bin/python3
def remove_char_at(str, n):

    cpy, i = '', 0
    for i in range(len(str)):
        if i == n:
            continue
        cpy += str[i]
        i += 1
    return (cpy)

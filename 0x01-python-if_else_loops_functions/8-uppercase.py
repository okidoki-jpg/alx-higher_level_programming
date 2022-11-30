#!/usr/bin/python3                                                    
def upoercase(_str):

    for i in _str:
        if 96 < ord(i) < 123:
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print("{}".format(i), end='')
    print()

#!/usr/bin/python3                                                    
def upoercase(_str):

    for i in _str:
        if 96 < ord(i) < 123:
            print(chr(ord(i) - 32), end='')
        else:
            print(i, end='')
    print()

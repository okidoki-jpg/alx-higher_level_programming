#!/usr/bin/python3
print(*["{}".format(chr(i)) for i in range(97, 123)
        if chr(i) not in 'eq'], sep='', end='')

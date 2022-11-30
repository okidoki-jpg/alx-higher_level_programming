#!/usr/bin/python3
n, no = 2, 0
for i in range(100):
    if (no != 0 and no % 10 == 0):
        no += n
        n += 1
    if no > 99:
        break
    print("{:02d}".format(no))
    no += 1

#!/usr/bin/python3
n, no = 2, 1
for i in range(100):
    if (no % 10 == 0):
        no += n
        n += 1
    print("{:02d}".format(no), end='')
    no += 1
    if no < 90:
        print(", ", end='')
        continue
    else:
        print()
        break

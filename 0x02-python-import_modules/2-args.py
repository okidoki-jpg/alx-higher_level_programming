#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    idx, var = len(argv), "argument"
    if idx < 2:
        print("0 arguments.")
    elif idx == 2:
        print("1 {}:".format(var))
        print("1: {}".format(argv[1]))
    else:
        var += 's'
        print("{:d} {}:".format(idx-1, var))
        for idx in range(1, idx):
            print("{:d}: {}".format(idx, argv[idx]))


#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print(sum([0 if len(argv) < 2 else int(i) for i in argv[1:]]))

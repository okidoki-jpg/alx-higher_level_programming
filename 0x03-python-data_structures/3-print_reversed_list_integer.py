#!/usr/bin/python3
if __name__ == "__main__":
    def print_reversed_list_integer(my_list=[]):
        [print("{:d}".format(i)) for i in my_list[::-1]]

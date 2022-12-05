#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):

        ny_string = my_string.translate({ord(i): None for i in "cC"})
        return my_string

#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):

        new_str = ""
        for idx in my_string:
            if idx not in "cC":
                new_str += idx
        return new_str

#!/usr/bin/python3
if __name__ == "__main__":
    def delete_at(my_list=[], idx=0):
        if idx > -1 and idx < len(my_list):
            del my_list[idx]
        return my_list

#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):

        if 0 > idx or idx > len(my_list):
            return
        return my_list[idx]

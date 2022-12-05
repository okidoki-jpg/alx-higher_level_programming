#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):

        if idx > -1 and idx < len(my_list):
            return my_list[idx]
        return None

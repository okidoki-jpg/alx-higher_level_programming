#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_ls = my_list[:]
    for i in range(len(new_ls)):
        if new_ls[i] == search:
             new_ls[new_ls.index(search)] = replace
    return new_ls

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for num in my_list:
        if num == search:
            my_list[my_list.index(num)] = replace
    return(my_list)

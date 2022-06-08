#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = my_list.copy()
    for num in mylist:
        if num == search:
            mylist[mylist.index(num)] = replace
    return(mylist)

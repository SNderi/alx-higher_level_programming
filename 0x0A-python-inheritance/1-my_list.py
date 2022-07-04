#!/usr/bin/python3
''' Inherit from list Module '''


class MyList(list):
    ''' Derived list class '''

    def print_sorted(self):
        ''' prints the list, but sorted (ascending sort) '''
        new = self[:]
        new.sort()
        print(new)

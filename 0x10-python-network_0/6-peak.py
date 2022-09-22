#!/usr/bin/python3
""" Module for a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ Find peak(greatest num) in a list of unsorted integers. """
    if type(list_of_integers) == list:
        if len(list_of_integers) == 0:
            return None
        return max(list_of_integers)
    return None

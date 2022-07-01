#!/usr/bin/python3
'''Module to print a square'''


def print_square(size):
    '''Prints a square using #

    Args:
        size (int): Length of square

    Raises:
        TypeError: if size is not an integer
                   if size is a negative float
                   ValueError: if size is less than 0
    '''

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    
    for i in range(size):
        print("#" * size)

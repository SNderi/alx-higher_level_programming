#!/usr/bin/python3
'''This module calculates sum of 2 integers'''


def add_integer(a, b=98):
    '''Adds 2 integers.

    Args:
        a: The first parameter
        b: The second parameter (Defaults to 98)

    Returns:
        int: Addition result

    Raises:
        TypeError: If a or b is not an integer

    '''
    allowed = [int, float]
    if type(a) not in allowed:
        raise TypeError('a must be an integer')
    if type(b) not in allowed:
        raise TypeError('b must be an integer')
    return(int(a) + int(b))

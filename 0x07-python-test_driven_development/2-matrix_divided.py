#!/usr/bin/python3
'''Module for matrix division'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix

    Args:
        matrix: Dividend list of lists of integers or floats
        div: Divisor

    Returns:
        matrix: Quotient list of lists

    Raises:
        ZeroDivisionError: If div is 0
        TypeError: If any of the dividends in not an integer or float
                 : If all rows aren't of the same size
                 : If div is not an integer or float
    '''

    allowed = [int, float]
    lists_len = []
    new_matrix = []

    if type(div) not in allowed:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        lists_len.append(len(row))
        for col in row:
            if type(col) not in allowed:
                raise TypeError('matrix must be a matrix (list of lists) ' +
                        'of integers/floats')

    if len(set(lists_len)) != 1:
        raise TypeError('Each row of the matrix must have the same size')

    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / div, 2))
    return new_matrix

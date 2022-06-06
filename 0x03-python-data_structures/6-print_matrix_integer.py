#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for num in l:
            print("{}".format(num), end=' ')
        print()

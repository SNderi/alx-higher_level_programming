#!/usr/bin/python3
""" Module MyInt inheriting from int """


class MyInt(int):
    ''' Inverts == and != '''

    def __eq__(self, other):
        ''' Inverts Equality '''
        return super().__ne__(other)

    def __ne__(self, other):
        ''' Inverts Inequality '''
        return super().__eq__(other)

#!/usr/bin/python3
''' Module BaseGeometry with improvements'''


class BaseGeometry():
    ''' BaseGeometry class
    Methods:
        Area:  raises an Exception
    Raises:
        Exception
    '''
    def area(self):
        ''' Raises an Exception '''
        raise Exception('area() is not implemented')

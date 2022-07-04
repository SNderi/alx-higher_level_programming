#!/usr/bin/python3
''' Module BaseGeometry with integer validation '''


class BaseGeometry():
    ''' BaseGeometry class
    Methods:
        Area:  raises an Exception
        integer_validator: Validates value
    '''
    def area(self):
        ''' Raises an Exception
        Raises:
            Exception
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates value
        Args:
            name (str): name of value
            value: argument to be validated

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is < or = 0
        '''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

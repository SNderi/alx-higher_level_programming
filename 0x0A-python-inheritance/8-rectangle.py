#!/usr/bin/python3
''' Module Rectangle inheriting from BaseGeometry '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Represents a rectangle inheriting from BaseGeometry
    Attr:
        Width
        Height
    '''
    def __init__(self, width, height):
        ''' Initializes an object
        Args:
            width: width of the rectangle
            heigth: height of the rectangle
        '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

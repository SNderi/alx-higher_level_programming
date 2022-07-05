#!/usr/bin/python3
''' Module for class student with instance dictionary representation '''


class Student:
    ''' Represents a student
    Attributes:
        first_name
        last_name
        age

    Methods:
        to_json: retrieves a dictionary representation of a Student instance
    '''

    def __init__(self, first_name, last_name, age):
        ''' initialize an instance
        Args:
            first_name
            last_name
            age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Retrieves a dictionary representation of a Student instance '''

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()

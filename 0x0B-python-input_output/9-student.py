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

    def to_json(self):
        ''' Retrieves a dictionary representation of a Student instance '''
        return self.__dict__

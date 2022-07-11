#!/usr/bin/python3
''' Module for the base class of this project '''


import json
import os


class Base:
    ''' “base” of all other classes in this project.
    It's goal is to manage id attribute in all classes in the project
    and to avoid duplicating the same code (by extension, same bugs)
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Class constructor '''

        if id is not None and type(id) == int:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns the JSON string representation of list_dictionaries '''

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
                not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes the JSON string representation of list_objs to a file '''

        if list_objs is None or list_objs == []:
            jst = "[]"
        else:
            jst = cls.to_json_string([ob.to_dictionary() for ob in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(jst)

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of the JSON string representation json_string '''

        if type(json_string) != str:
            raise TypeError('json_string should be a string')
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Returns an instance with all attributes already set '''

        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 3)
        elif cls.__name__ == 'Square':
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances '''

        filename = cls.__name__ + ".json"
        lst = []
        dlist = []
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                s = file.read()
                dlist = cls.from_json_string(s)
                for d in dlist:
                    lst.append(cls.create(**d))
        return lst

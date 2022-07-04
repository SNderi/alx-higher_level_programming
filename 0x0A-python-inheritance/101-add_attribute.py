#!/usr/bin/python3
''' Module that adds a new attribute to an object '''


def add_attribute(obj, attr, val):
    ''' Checks if it is possible to add an attribute with value val
    to object obj.

    Args:
        obj: object to add the attribute to
        attr: name of the attribute
        val: value of the attribute to add
    '''

    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)

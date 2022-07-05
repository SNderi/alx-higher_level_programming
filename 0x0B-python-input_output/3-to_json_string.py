#!/usr/bin/python3
''' Module to serialize a string '''


def to_json_string(my_obj):
    '''  Returns the JSON representation of an object (string) '''
    import json
    return json.dumps(my_obj)

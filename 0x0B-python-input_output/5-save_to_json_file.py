#!/usr/bin/python3
''' Module to write an object to a text file '''


def save_to_json_file(my_obj, filename):
    '''  Writes an Object to a text file, using a JSON representation '''
    import json
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

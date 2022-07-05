#!/usr/bin/python3
''' Module to load, add and save arguments to a Python list '''


import sys
import json
import os.path

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


file = 'add_item.json'

if os.path.isfile(file):
    arg_list = load(file)
else:
    arg_list = []

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        arg_list.apend(arg)

save(arg_list, file)

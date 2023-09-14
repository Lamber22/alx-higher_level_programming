#!/usr/bin/python3


"""A JSON function that writes to text file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a tex file using JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

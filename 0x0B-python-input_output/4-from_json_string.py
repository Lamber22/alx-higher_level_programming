#!/usr/bin/python3


"""Defines a JSON to objects function"""


import json


def from_json_string(my_str):
    """Returns a an object(pyhton data structure) represented by json"""
    return json.loads(my_str)

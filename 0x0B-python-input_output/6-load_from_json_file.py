#!/usr/bin/python3


"""Defines a function that creates objects from JSON file"""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, encoding="utf8") as f:
        return json.load(f)

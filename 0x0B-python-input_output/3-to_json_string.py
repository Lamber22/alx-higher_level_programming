#!/usr/bin/python3


"""Defines a string to json function"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    return json.dumps(my_obj)

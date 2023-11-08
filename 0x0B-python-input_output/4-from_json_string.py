#!/usr/bin/python3


"""Defines a function that return an object represented by json"""
import json


def from_json_string(my_str):
    """Decode a string"""
    return json.loads(my_str)

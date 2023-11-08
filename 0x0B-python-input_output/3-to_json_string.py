#!/usr/bin/python3


"""Defines a function that returns JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Returns json string representation"""
    return json.dumps(my_obj)

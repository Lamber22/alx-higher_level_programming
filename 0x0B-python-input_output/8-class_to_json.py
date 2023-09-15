#!/usr/bin/python3


"""Defines a function that returns class to JSON"""


def class_to_json(obj):
    """Returnas the dictionary description with simple data structure"""
    return obj.__dict__

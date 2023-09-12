#!/usr/bin/python3


"""Defines a class that checks for certain condition"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check
        a_ class (type): The class to match the type of obj to .
    Return:
        If obj is exactly an instance of a_class: return True.
        Else: return False
    """
    if type(obj) == a_class:
        return True
    return False

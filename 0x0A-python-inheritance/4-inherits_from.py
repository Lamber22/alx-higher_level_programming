#!/usr/bin/python3


"""Defines a class inherited function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj - Object to check
        a_class(type) - Class to match the type of obj to
    Returns:
        True - If obj is an inherited instance of a_class.
        False - Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

#!/usr/bin/python3


"""Defines a inherited class checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj - The object to check
        a_class (type) - The class to match the type of obj to
    Returns:
        True - If obj is an instance or inherited of a_class.
        False - Otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False

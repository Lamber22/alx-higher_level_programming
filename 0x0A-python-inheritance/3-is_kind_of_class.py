#!/usr/bin/python3


"""defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class
    Args:
        obj (any): The class to match the type of obj to.
    Return:
        If obj is an instance or inherited instance of a_clss: return True
    Else: return False
    """
    if isinstance(obj, a_class):
        return True
    return False

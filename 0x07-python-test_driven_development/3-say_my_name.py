#!/usr/bin/python3

"""Defines a name printing function"""


def say_my_name(first_name, last_name):
    """ Prints the first and last name of a person.

    Args:
        str(first_name) - The first name
        str(last_name) - The last name

    Raises:
    TypeError: if the first and last name are not strings

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

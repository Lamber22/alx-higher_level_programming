#!/usr/bin/python3


"""Defines a Locked Class"""


class LockedClass:
    """
    Prevents the user from dynamically creating a new instance attributes
    except for instance attribute called first_name.
    """

    __slots__ = ['first_name']

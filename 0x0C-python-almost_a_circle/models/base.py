#!/usr/bin/python3


"""Defines a Base class"""


class Base:
    """Represents a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Iniitalizes a new base

        Args:
            id(int) - The identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

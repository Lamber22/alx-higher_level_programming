#!/usr/bin/python3

import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json serialization of a list of dicts

        Args:
           list_dictionaries(list): Represtents the list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

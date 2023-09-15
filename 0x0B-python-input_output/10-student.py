#!/usr/bin/python3


"""A Student to JSON class with filter"""


class Student:
    """A Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of a Student instance

        If attrs is a list of strings, represents only those included
        in the list.

        Args:
            attrs (list): (Optional) The attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

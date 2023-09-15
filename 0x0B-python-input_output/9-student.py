#!/usr/bin/python3

"""Student to JSON function"""


class Student:
    """Defines a Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of Studrnt class"""
        return self.__dict__

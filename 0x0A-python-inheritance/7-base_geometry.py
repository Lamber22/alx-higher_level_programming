#!/usr/bin/python3


"""Defines a Geometry class"""


class BaseGeometry:
    """Represents a Geometry"""

    def area(self):
        """Represents the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the Geometry value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if (value <= 0):
            raise ValueError("<name> must be greater than 0")

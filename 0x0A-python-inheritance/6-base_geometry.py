#!/usr/bin/python3


"""Defines a Geometry class"""


class BaseGeometry:
    """Represents a Geometry"""

    def area(self):
        """The area of the geometry"""
        raise Exception("area() is not implemented")

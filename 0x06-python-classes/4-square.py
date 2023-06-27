#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize and reserves data
        Arg:
        size(int) - the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return(self.__size * self.__size)

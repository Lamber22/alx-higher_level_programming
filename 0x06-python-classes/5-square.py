#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes and reserves data
        Arg:
        size(int) - the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get/retrieve the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Arg: value(int) - the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square to stdout of # character"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)

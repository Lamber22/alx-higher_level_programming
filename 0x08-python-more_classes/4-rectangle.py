#!/usr/bin/python3

"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the rectangle

        Represents the rectangle with a 3 character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        res = []
        for i in range(self.__height):
            [res.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                res.append("\n")
        return ("".join(res))

    def __repr__(self):
        """Return the string representation of the rectangle"""
        res = "Rectangle(" + str(self.__width)
        res += ", " + str(self.__height) + ")"
        return (res)
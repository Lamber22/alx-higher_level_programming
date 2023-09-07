#!/usr/bin/python3

"""A function that prints a square with a # character"""


def print_square(size):
    """Prints a sqaure.

    Args:
        size - The size of the square
    
    raises:
        TypeError - if size not an integer
        ValueError - if size is less than 0
        TypeError - if size is a float, size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for l in range(size)]
        print("")

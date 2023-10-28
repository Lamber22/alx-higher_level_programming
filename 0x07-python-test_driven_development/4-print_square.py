#!/usr/bin/python3


"""Defines a function that prints a square using '#' character"""


def print_square(size):
    """Prints a square with a '#' character.

    Args:
        size(int) - The length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: - if size is less than zero
        TypeError: - if size is (float) and less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

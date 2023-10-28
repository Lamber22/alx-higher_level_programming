#!/usr/bin/python3



def add_integer(a, b=98):
    """ A function that adds 2 integers

    Args:
        int(a) - The first integer
        int(b) - The second integer

    Raises:
        TypeError: if a and b are not integer or float

    Return:
        a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return a + b

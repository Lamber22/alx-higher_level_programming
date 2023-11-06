#!/usr/bin/python3


"""A class that inherits from list"""


class MyList(list):
    """Inherits from list"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print (sorted(self))

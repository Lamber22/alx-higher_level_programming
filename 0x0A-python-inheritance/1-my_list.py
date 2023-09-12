#!/usr/bin/python3


"""Defines an herited list class MyList"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Prints alist in sorted order"""
        print(sorted(self))

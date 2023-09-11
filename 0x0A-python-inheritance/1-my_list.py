#!/usr/bin/python3


"""Defines a class that will be inherited"""


class Mylist(list):
    """Implements sorted printing for the built - in liat class"""

    def print_sorted(self):
        """Prints alist in sorted order"""
        print(sorted(self))

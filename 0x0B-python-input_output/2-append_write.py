#!/usr/bin/python3


"""Defines a function that appends to a file"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)

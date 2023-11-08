#!/usr/bin/python3


"""Defines a function that writes to a file"""


def write_file(filename="", text=""):
    """Writes to a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)

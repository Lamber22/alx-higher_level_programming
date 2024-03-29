#!/usr/bin/python3


"""Defines a function that reads from a text file"""


def read_file(filename=""):
    """Prints the content of a file to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

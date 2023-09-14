#!/usr/bin/python3


""" A function that reads a file and prints to stdout"""


def read_file(filename=""):
    """Prints the content of a UTF8 tet file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

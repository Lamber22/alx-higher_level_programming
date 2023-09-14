#!/usr/bin/python3


"""Deines a function that appends"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.
    filename: The name of the file to append to.
    text (str): The string toappend to the file

    Return: The number of characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

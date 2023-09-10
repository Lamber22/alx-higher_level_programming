#!/usr/bin/python3

""" Defines a text_indentation function"""


def text_indentation(text):
    """
    Prints a text with two lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print
    Raises:
        TypeError: I the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1

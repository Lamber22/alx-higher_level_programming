#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """This function return a set of all elements present in only one set."""
    return (set_1 ^ set_2)

#!/usr/bin/python3

def uniq_add(my_list=[]):
    """This functio add all unique integers in a list
       (once for each integer)."""
    result = 0
    for x in set(my_list):
        result += x
    return (result)

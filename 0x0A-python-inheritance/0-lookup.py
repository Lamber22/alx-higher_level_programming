#!/usr/bin/python3

"""Defines an object attribute function."""


def lookup(obj):
    """This function return a list of an object available attributes"""
    return (dir(obj))

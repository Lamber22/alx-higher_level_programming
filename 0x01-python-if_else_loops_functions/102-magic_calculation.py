#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Matching bytecode provided by ALX."""
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b - c)

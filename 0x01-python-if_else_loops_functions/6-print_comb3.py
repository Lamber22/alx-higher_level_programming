#!/usr/bin/python3
"""
This function prints the combination of all possible numbers
n1 is for the first number
n2 is for the second number"""

for n1 in range(0, 10):
    for n2 in range(n1 + 1, 10):
        if n1 == 8 and n2 == 9:
            print("{}{}".format(n1, n2))
        else:
            print("{}{}".format(n1, n2), end=", ")

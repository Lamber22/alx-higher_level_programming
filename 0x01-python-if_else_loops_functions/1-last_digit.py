#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
"""This function prints the last digit of any number it generates
storing the last digit in the variable l_digit
"""
l_digit = abs(number) % 10
if number < 0:
    l_digit = -l_digit
if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif l_digit == 0:
    print(f"The last digit of {number} is {l_digit} and is 0")
elif l_digit < 6 and not 0:
    print(f"The last digit of {number} is {l_digit} and is less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_str = repr(number)
last_d = n_str[-1]
# convert the last digit into an integer
last_d = int(last_d)
# print the last digit
print("Last digit of {0} is {1}".format(number, last_d))

if last_d > 5:
    print("{} and is greater than 5".format(number))
elif last_d == 0:
    print("{} and is 0".format(number))
elif last_d < 6 and not 0:
    print("{} and is less than 6 and not 0".format(number))

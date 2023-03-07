#!/usr/bin/python3
#  prints the ASCII alphabet, in lowercase, not followed by a new line
# Print all the letters except q and e
for ch in range(97, 123):
    if chr(ch) is not 'q' and chr(ch) is not 'e':
        print("{}".format(chr(ch)), end="")

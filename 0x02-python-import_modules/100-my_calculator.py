#!/usr/bin/python3

if __name__ == "__main__":
    """This function handles basic operations"""
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    oprs = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(oprs.keys()):
        print("Unknown operator. Available operators: +, -, * and /")

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, oprs[sys.argv[2]](a, b)))

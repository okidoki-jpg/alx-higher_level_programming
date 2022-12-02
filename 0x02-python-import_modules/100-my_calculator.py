#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    
    ops = ["+", "-", "*", "/"]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a, b, op = int(argv[1]), int(argv[3]), str(argv[2])
        if (argv[2] == "+"):
            print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b))) 
        if (argv[2] == "-"):
            print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b))) 
        if (argv[2] == "*"):
            print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b))) 
        if (argv[2] == "/"):
            print("{:d} {} {:d} = {:d}".format(a, op, b, div(a, b))) 

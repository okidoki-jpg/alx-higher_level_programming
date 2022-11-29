#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10

print(f"Last digit of {number} is {n} and is", end = " ")
if n > 5:
    print("greater than 5")
elif n == 0:
    print("0")
elif n < 6:
    print("less than 6 and is not 0")


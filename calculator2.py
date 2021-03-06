"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic2 import *


# Your code goes here
while True:
    user_input = input("Enter the calculation type and numbers separated by space: ")
    tokens = user_input.split(" ")
    numbers = []
    for token in tokens[1:]:
        numbers.append(float(token))

    if tokens[0] == 'q':
        break
    elif tokens[0] == '+':
        print(add(numbers))
    elif tokens[0] == '-':
        print(subtract(float(tokens[1]),float(tokens[2])))
    elif tokens[0] == '*':
        print(multiply(float(tokens[1]),float(tokens[2])))
    elif tokens[0] == '/':
        print(divide(float(tokens[1]),float(tokens[2])))
    elif tokens[0] == 'square':
        print(square(numbers))
    elif tokens[0] == 'cube':
        print(cube(float(tokens[1])))
    elif tokens[0] == 'pow':
        print(power(float(tokens[1]),float(tokens[2])))
    elif tokens[0] == 'mod':
        print(mod(float(tokens[1]),float(tokens[2])))


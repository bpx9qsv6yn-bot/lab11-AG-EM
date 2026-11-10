# https://github.com/EshuMarneedi/lab11-EM-AG
# Partner 1: Eshan Marneedi
# Partner 2: Ansh Gupta

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    try:
        if a == 0:
            raise ZeroDivisionError
        
        return b / a 
    except ZeroDivisionError as e:
        print(e)

def logarithm(a, b): 
    try:
        if a <= 0:
            raise ValueError
        
        return math.log(a, b)
    except ValueError as e:
        print(e)

def exponent(a, b):
    return a ** b

import math

def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def log(a, b): 
    try:
        if a<=0:
            raise ValueError
        return math.log(a,b)
    except ValueError as e:
        print(e)

def exp(a, b): 
    return a**b

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        
        return math.sqrt(a)
    except ValueError as e:
        print(e)

def hypotenuse(a, b):
    return math.hypot(a, b)
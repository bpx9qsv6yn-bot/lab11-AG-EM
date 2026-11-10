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
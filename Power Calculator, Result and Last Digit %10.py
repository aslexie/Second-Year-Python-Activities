# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:07:41 2024

@author: alexandria
"""

def last_digit_power(base, exponent):
    if exponent == 0:
        return 1
    base %= 10
    if base == 0:
        return 0
    if base == 1 or base == 5 or base == 6:
        return base
    if exponent % 4 == 1:
        return base
    if exponent % 4 == 2:
        return (base * base) % 10
    if exponent % 4 == 3:
        return (base * base * base) % 10
    return (base * base * base * base) % 10

base = 2
exponent = int(input("Enter the exponent: "))
power = base ** exponent
last_digit = power % 10

print("Result:", power)
print("Last digit of 2 raised to the power of", exponent, "is:", last_digit)


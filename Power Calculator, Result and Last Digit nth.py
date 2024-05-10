# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:10:09 2024

@author: alexandria
"""

def last_digit_power(base, exponent):
    if exponent == 0:
        return 1
    base %= 100
    if base == 0:
        return 0
    if base == 1 or base == 5 or base == 6:
        return base
    if exponent % 4 == 1:
        return base
    if exponent % 4 == 2:
        return (base * base) % 100
    if exponent % 4 == 3:
        return (base * base * base) % 100
    return (base * base * base * base) % 100

exponent = int(input("Enter the exponent: "))
digits = int(input("Enter the number of digits you want: "))

base = 2
power = base ** exponent
last_digit = power % (10 ** digits)

print("Result of 2 raised to the power of", exponent, "is:", power)
print("Last", digits, "digits of 2 raised to the power of", exponent, "is:", last_digit)

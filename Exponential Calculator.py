# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:57:38 2024

@author: alexandria
"""

print("THE POWER PLAY CALCULATOR!")
print("Welcome to the Exponential Calculator!")
print("Simply input the base and the exponent to get the result.\n")

while True:
    base = input("Enter the base value (or 0 to exit): ")
    if base == '0':
        print("\nThank you for using the Exponential Calculator!")
        print("I hope you had fun! Goodbye!")
        break
    else:
        base = float(base)
        exponent = float(input("Enter the exponent value: "))
        print(f"{base} to the power of {exponent} is {base**exponent}\n")

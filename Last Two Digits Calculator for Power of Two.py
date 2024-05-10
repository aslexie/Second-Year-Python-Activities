# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:14:41 2024

@author: alexandria
"""

power = int(input("Enter the power: "))
result = pow(2, power) % 100
print("The last digit of 2 raised to the power of", power, "is", result)

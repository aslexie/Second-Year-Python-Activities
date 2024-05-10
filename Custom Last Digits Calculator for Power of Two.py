# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:15:16 2024

@author: alexandria
"""

power = int(input("Enter the power: "))
digits = int(input("Enter the number of digits: "))
result = str(2**power)[-digits:]
print("The last", digits, "digits of 2 raised to the power", power, "is", result)


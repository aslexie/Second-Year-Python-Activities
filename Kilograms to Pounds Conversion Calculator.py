# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:39:34 2024

@author: alexandria
"""

def kg_to_pounds(kg):
    pounds = kg * 2.20462
    return pounds

kg = float(input("Enter weight in kilograms: "))
pounds = kg_to_pounds(kg)
print(f"The weight in pounds is {pounds}")

# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:47:47 2024

@author: alexandria
"""

def number_operations():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The first number is {num1}")
    print(f"The second number is {num2}")
    product = num1 * num2
    if product <= 1000:
        print(f"The product of the two numbers is {product}\n")
    else:
        sum = num1 + num2
        print(f"The sum of the two numbers is {sum}\n")

print("THE NUMBER OPERATIONS CHALLENGE!\n")

print("First given:")
number_operations()

print("Second given:")
number_operations()

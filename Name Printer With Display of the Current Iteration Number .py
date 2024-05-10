# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:19:04 2024

@author: alexandria
"""

name = input("What's your name? ")
count = eval(input("How many times would you like to print your name? "))

for i in range(count):
    print(str(i+1) + ". " + name)

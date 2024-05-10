# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:19:42 2024

@author: alexandria
"""

n = eval(input("How many Fibonacci numbers would you like to print? "))

fib = [1, 1]

for i in range(2, n):
    next_num = fib[i-1] + fib[i-2]
    fib.append(next_num)

for i in range(n):
    print(fib[i])

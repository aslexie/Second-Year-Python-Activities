# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:03:46 2024

@author: alexandria
"""

import random

numbers = []
for i in range(5):
    numbers.append(round(random.uniform(1, 100), 2))

average = sum(numbers) / len(numbers)

print("Random numbers:", numbers)
print("Average:", average)

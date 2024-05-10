# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:45:05 2024

@author: alexandria
"""

from random import randint

print("THE MULTIPLICATION MASTERY CHALLENGE!")
print("Practice your multiplication skills here! (Basic Level)\n")

score = 0

for i in range(1, 11):
    x = randint(1, 10)
    y = randint(1, 10)
    correct_answer = x * y

    print(f"\nQuestion #{i}:")
    print(f"{x} x {y} = ")
    user_answer = int(input("Answer: "))

    if user_answer == correct_answer:
        score += 1
        print("Right!")
    else:
        print(f"Wrong. The answer is {correct_answer}")

print(f"\n\nScore: {score} / 10")

# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:43:01 2024

@author: alexandria
"""

from random import randint

print("THE NUMBER GUESSING CHALLENGE!")
print("Guess a random number from 1 to 20. You have 3 chances.\n")

random_number = randint(1, 20)

for i in range(3):
    guess = int(input("Type your guess here: "))
    
    if guess == random_number:
        print("Congratulations! You guessed the number!\n")
        break
    elif i < 2:
        print("Oops, Try Again!\n")
    else:
        print(f"Game Over! The random number was {random_number}.\n")

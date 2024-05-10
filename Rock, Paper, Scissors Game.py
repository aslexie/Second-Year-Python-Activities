# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:28:28 2024

@author: alexandria
"""

from random import choice

game = ["ROCK", "PAPER", "SCISSORS"]
rules = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}

print("Welcome to Rock, Paper, and Scissors Game!\n")

x = int(input("How many times do you want to play?: "))
score = 0

for i in range(x):
    print(f"\nRound {i+1}:\n")
    player_input = input("Type your choice between ROCK, PAPER, or SCISSORS (use capital letters only): ")
    computer_player = choice(game)
    print("Computer Answer: ", computer_player)

    if player_input == computer_player:
        print("It's a draw")
    elif rules[player_input] == computer_player:
        score += 1
        print("You won!")
    else:
        print("The computer won!")

print("\nYour score: ", score, "/", x)

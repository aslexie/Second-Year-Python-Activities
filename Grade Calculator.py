# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:59:37 2024

@author: alexandria
"""

print("Welcome to the Grade Calculator!")
print("Simply input the number of subjects and the grades to get the average.\n")

from random import randint

grades_sum = 0
num_subjects = int(input("How many subjects did you have last semester?: "))

for _ in range(num_subjects):
    subject = input("Name of the subject: ")
    grade = float(input("Grade: "))
    grades_sum += grade

average = grades_sum / num_subjects
print(f"Your average last semester is {round(average, 2)}\n")

print("Average Prediction\n")

grade_ranges = [(97, 100), (94, 96), (90, 93), (85, 89), (80, 84), (75, 79), (0, 74)]
for grade_range in grade_ranges:
    if grade_range[0] <= average <= grade_range[1]:
        predicted_average = (randint(*grade_range) + average) / 2
        print(f"Your predicted average is {predicted_average}")
        break

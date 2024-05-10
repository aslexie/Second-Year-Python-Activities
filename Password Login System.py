# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:46:54 2024

@author: alexandria
"""

password = 12345
attempts = 5

print("THE SECURE LOGIN SYSTEM!\n")

while attempts > 0:
    entered_password = int(input("Enter your password: "))
    attempts -= 1

    if entered_password != password:
        print("Wrong password! Try Again!")
        print(f"You only have {attempts} attempt{'s' if attempts > 1 else ''} left.\n")
        if attempts == 0:
            print("You are now kicked off the system.")
    else:
        print("You are now logged in to the system.")
        break

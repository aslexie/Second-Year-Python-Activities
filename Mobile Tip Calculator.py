# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:22:18 2024

@author: alexandria
"""

meal_price = float(input("Enter the price of the meal: "))
tip_percent = float(input("Enter the percent tip: "))

tip_amount = meal_price * (tip_percent / 100)
total_bill = meal_price + tip_amount

print("Tip amount:", tip_amount)
print("Total bill:", total_bill)

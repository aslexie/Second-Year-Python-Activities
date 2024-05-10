# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:53:01 2024

@author: alexandria
"""

menu = {
    "A": {"description": "Burger", "price": 100.00},
    "B": {"description": "Fries", "price": 50.00},
    "C": {"description": "Soft Drink", "price": 40.00}
}

print("THE FAST FOOD ORDER SYSTEM!\n")
print("\tCode\t\tDescription\t\tPrice")
for code, item in menu.items():
    print(f"\t[{code}]\t\t\t{item['description']}\t\tP{item['price']}")

total = 0
order = int(input("How many items do you want to order?"))

for _ in range(order):
    code = input("Type the Code of your Choice:").upper()
    quantity = int(input("Type the quantity of your order:"))
    
    if code in menu:
        item_total = menu[code]['price'] * quantity
        print(f"{quantity} {menu[code]['description']} P{item_total:.2f}")
        total += item_total
    else:
        print("Invalid code!")

print("Total Purchase: P{:.2f}".format(total))

payment = float(input("Payment Amount: "))

while payment < total:
    print("Insufficient amount! Try again!")
    payment = float(input("Payment Amount: "))

print("Your change is P{:.2f}".format(payment - total))
print("\nThank you for your order!")

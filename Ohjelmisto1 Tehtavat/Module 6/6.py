import math

def calculate_unit_price(diameter, price):
    A = (math.pi * (diameter / 100 / 2) ** 2)
    pricePerUnit = price / A
    return pricePerUnit

First_unit_price = calculate_unit_price(float(input("Enter the diameter of the first pizza (cm): ")), float(input("Enter the price of the first pizza (euros): ")))
Second_unit_price = calculate_unit_price(float(input("Enter the diameter of the second pizza (cm): ")), float(input("Enter the price of the second pizza (euros): ")))
print(f"Unit price of the first pizza: {First_unit_price:.2f} euros/m²")
print(f"Unit price of the second pizza: {Second_unit_price:.2f} euros/m²")
if First_unit_price > Second_unit_price:
    print("The second pizza provides better value for money.")
else:
    print("The first pizza provides better value for money.")
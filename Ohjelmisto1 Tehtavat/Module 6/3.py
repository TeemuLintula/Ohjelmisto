liters = 0
gallons = 0
def gallons_to_liters(gallons):
    liters = gallons * 3.785
    return liters

while True:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
    liters = gallons_to_liters(gallons)
    if liters < 0:
        break
    print(gallons, f"American gallons is {liters:.2f} liters.")
print("Program finished.")
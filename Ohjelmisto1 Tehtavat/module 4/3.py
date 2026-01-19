luku = input("Enter a number (or press Enter to quit): ")
smallest = float(luku)
biggest = float(luku)
while luku != "":
    luku = float(luku)
    if luku < smallest:
        smallest = luku
    if luku > biggest:
        biggest = luku
    luku = input("Enter a number (or press Enter to quit): ")
print("Smallest number:", smallest)
print("Largest number:", biggest)
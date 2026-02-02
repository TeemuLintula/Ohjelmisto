name = input("Enter a name: ")
names = set()
while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter a name: ")
print("Names you entered:", names)
username = input("Enter username: ")
password = input("Enter password: ")
correctusername = "python"
correctpassword = "rules"
tries = 1
while username != correctusername or password != correctpassword:
    if tries == 5:
        break
    print("Incorrect username or password. Please try again.")
    username = input("Enter username: ")
    password = input("Enter password: ")
    tries += 1
if tries == 5:
    print("Access denied")
else:
    print("Welcome")
number = int(input("Enter an integer: "))
isprime = True
if number < 2:
    isprime = False
    print(number, "is not a prime number.")
for i in range(2, number):
    if number % i == 0:
        isprime = False
        print(number, "is not a prime number.")
        break
if isprime:
    print(number, "is a prime number.")
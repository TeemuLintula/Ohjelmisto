num = input("Enter a number: ")
numbers = []
while True:
    if num == "":
        break
    num = float(num)
    numbers.append(num)
    num = input("Enter a number: ")
numbers.sort(reverse=True)
print("The greatest numbers in descending order: ")
for i in range(0, 5):
    if i < len(numbers):
        print(numbers[i])
import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)

num11=random.randint(1,6)
num12=random.randint(1,6)
num13=random.randint(1,6)
num14=random.randint(1,6)


digit_code3 = str(num1) + str(num2) + str(num3)
digit_code4 = str(num11) + str(num12) + str(num13) + str(num14)

print("3-digit code:", digit_code3)
print("4-digit code:", digit_code4)
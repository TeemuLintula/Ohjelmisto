import random

N = int(input("how many dots: "))
x=0
n=0
while x < N:
     if (random.uniform(-1, 1) ** 2 + random.uniform(-1, 1) ** 2) < 1:
        n += 1
     x +=1
pii = 4 * n / N
print("Approximation of pi:", pii)
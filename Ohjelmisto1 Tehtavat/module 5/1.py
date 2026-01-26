import random

Amount = int(input("How many dice to roll: "))
dices = list(range(1, Amount+1))
sum = 0

for single_dice in dices:
    single_dice = random.randint(1, 6)
    sum += single_dice

print("Sum of the dice: " + str(sum))
import random
noppa = 1
def roll_dice():
    return random.randint(1,6)
while noppa != 6:
    noppa = roll_dice()
    print(noppa)
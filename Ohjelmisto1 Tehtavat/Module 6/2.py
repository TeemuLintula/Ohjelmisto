import random
maxnum = int(input("Enter the maximum: "))
noppa = 1
def roll_dice(max):
    return random.randint(1,max)
while noppa != maxnum:
    noppa = roll_dice(maxnum)
    print(noppa)
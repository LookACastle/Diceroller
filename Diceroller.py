import random
def roll(dice, rools):
    dSum = 0
    for x in range(rools):
        dSum += random.randint(1, dice)
    return(dSum)

print(roll(4, 3))

import random

#Dice function
def roll(dice_sides, rolls):
    dice_sum = 0
    for x in range(rolls):
        dice_sum += random.randint(1, dice_sides)
    return(dice_sum)

#Debugging print
print(roll(4, 3))

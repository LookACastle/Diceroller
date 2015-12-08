import random
import re

#Get variables from input string
def read_input_string(input_string):
    if not "d" in input_string.lower():
        raise ValueError("Input must be in the format [rolls]d[sides]+/-[Modifiers]")

    number_of_rolls, rest = input_string.lower().split("d")
    number_of_rolls = int(number_of_rolls)

    operator_index = re.search("\+|-", rest)

    if operator_index:
        add_sum = int(rest[operator_index.start():])
        dice_size = int(rest[:operator_index.start()])
    else:
        add_sum = None
        dice_size = int(rest)

    return number_of_rolls, dice_size, add_sum

#Dice function
def roll(dice_sides, rolls):
    dice_sum = 0
    for x in range(rolls):
        dice_sum += random.randint(1, dice_sides)
    return(dice_sum)

#Debugging print
print(roll(4, 3))

input_string = raw_input("Dice roll: ")

print read_input_string(input_string)

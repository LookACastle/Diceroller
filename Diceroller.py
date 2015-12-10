import random
import re

#Get variables from input string
def read_input_string(input_string):
    if not "d" in input_string.lower():
        raise ValueError("Input must be in the format [rolls]d[sides]+/-[Modifiers]")

    number_of_rolls, rest = input_string.lower().split("d")
    number_of_rolls = int(number_of_rolls)

    if "w" in rest:
        rest, weapon_id = rest.split("w")
    else:
        weapon_id = None

    operator_index = re.search("\+|-", rest)

    if operator_index:
        add_sum = int(rest[operator_index.start():])
        dice_size = int(rest[:operator_index.start()])
    else:
        add_sum = None
        dice_size = int(rest)

    return number_of_rolls, dice_size, add_sum, weapon_id

#Dice function
def roll(dice_sides, rolls):
    dice_sum = 0
    for x in range(rolls):
        curr_roll = random.randint(1, dice_sides)
        dice_sum += curr_roll
        print "you rolled a:", curr_roll, "on roll no.", x+1

        #Crits and fumbles
        if dice_sides == 20 and dice_sum == 1 and rolls == 1:
            dice_sum = "a fumble!"
        elif dice_sides == 20 and dice_sum == 20 and rolls == 1:
            dice_sum = "a crit!"
    return(dice_sum)

#Debugging print
"""
print(roll(4, 3))
"""

#Runs the functions
while True:
    input_string = raw_input("Dice roll: ")

    number_of_rolls, dice_size, add_sum, weapon_id = read_input_string(input_string)

    sum = roll(dice_size, number_of_rolls)
    if sum not in ["a crit!", "a fumble!"] and add_sum:
        sum += add_sum

    print "You rolled a total of: ", sum
    if weapon_id:
        print weapon_id

import random
import re

#Get variables from input string
def read_input_string(input_string):
    if not "d" in input_string.lower():
        raise ValueError("Input must be in the format [rolls]d[sides]+/-[Modifiers]")

    number_of_rolls, rest = input_string.lower().split("d")

    #Turn individual rolls on or off
    if "i" in rest:
        rest, individual_rolls = rest.split("i")
        individual_rolls = True
    else:
        individual_rolls = False


    #Adding weapon support
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

    number_of_rolls = int(number_of_rolls)

    return number_of_rolls, dice_size, add_sum, weapon_id, individual_rolls

#Dice function
def roll(dice_sides, rolls, individual_rolls):
    dice_sum = 0
    for x in range(rolls):
        curr_roll = random.randint(1, dice_sides)
        dice_sum += curr_roll
        if dice_sides == 20 and curr_roll == 20 and individual_rolls:
            print "you rolled a crit on roll no.", x+1
        elif dice_sides == 20 and curr_roll == 1 and individual_rolls:
            print "you rolled a fumble on roll no.", x+1
        elif individual_rolls:
            print "you rolled a:", curr_roll, "on roll no.", x+1
        else:
            pass

        #Crits and fumbles
        if dice_sides == 20 and dice_sum == 1 and rolls == 1:
            luck = "bad"
        elif dice_sides == 20 and dice_sum == 20 and rolls == 1:
            luck = "good"
        else:
            luck = None
    return(dice_sum, luck)

print "format is: [amount of dice]d[sides on dice][+/-/" " a number to add or substract at the ende][i/" " to show every single throw]"

#Runs the functions
while True:
    input_string = raw_input("Dice roll: ")

    if input_string:
        number_of_rolls, dice_size, add_sum, weapon_id, individual_rolls = read_input_string(input_string)

        sum, luck = roll(dice_size, number_of_rolls, individual_rolls)
        if sum not in ["a crit!", "a fumble!"] and add_sum:
            sum += add_sum

        if luck == None:
            print "You rolled a total of: ", sum
        elif luck == "good":
            print "You rolled a critical hit!"
        elif luck == "bad":
            print "You rolled a fumble!"

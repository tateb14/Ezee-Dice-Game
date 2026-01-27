import random
def main():
    # main accepts no args
    # Calls all functions to play the number of games specified
    print("Welcome to the number dice game!")
    print("Do you want to start")
    roll_num = 1
    
    dice_list = first_roll()
    output_dice(dice_list, roll_num)
    mode = find_mode(dice_list)
    dice_list = reroll_many(dice_list, mode, roll_num)
    target_list = [mode] * 12
    while dice_list != target_list:
        dice_list = reroll_many(dice_list, mode, roll_num)
        roll_num += 1
        print()
    
    

def output_dice(dice_list, roll_num):
    # Accepts dice
    # Outputs each dice in the list to the console
    print(f"Roll {roll_num}:")
    print("-----------")
    index = 1
    for dice in dice_list:
        print(f"Dice {index}: {dice}")
        index += 1
    

def roll_die():
    import random
    dice = random.randint(1,6)
    return dice

def first_roll():
    import random
    dice_list = []
    for dice in range(12):
        dice_list.append(roll_die())
    return dice_list
    
    

def count_frequency(dice, target_number):
    # Accepts a list of 12 random integers and a target value
    # Returns how often that target value occurs in the list
    count = 0
    
    for die in dice:
        if die == target_number:
           count += 1
    return count

def find_mode(dice):
    # Accepts a list of dice.
    # Uses count_frequency(dice, target_number) to determine how often each number occurs.
    # Returns the mode
    dice_numbers = [1, 2, 3, 4, 5, 6]
    mode = 0
    mode_count = 0
    for die in dice_numbers:
        count = count_frequency(dice, die)
        if mode_count < count:
            mode_count = count
            mode = die
    return mode

def list_unmatched_dice(dice, mode):
    # Accepts a list of dice and list
    # Determines which dice need rerolled
    # Returns a list of indexes to reroll
    reroll_list = []
    index = 0
    for die in dice:
        if die != mode:
            print(index)
            reroll_list.append(index)
        index += 1
    return reroll_list

def reroll_one(dice, index):
    # Accepts a list of dice and an index.
    # Uses roll_die to reroll that index
    # Returns a new list with that index rerolled
    new_num = roll_die()
    dice[index] = new_num
    return dice

def reroll_many(dice, mode, roll_num):
    # Accepts a list of dice
    # Calls list_unmatched_dice() and reroll_one() to reroll each die != the mode.
    # Returns a list of rerolled dice.
    reroll_list = list_unmatched_dice(dice, mode)
    for reroll_index in reroll_list:
        dice = reroll_one(dice, reroll_index)
    output_dice(dice, roll_num)
    return dice
main()

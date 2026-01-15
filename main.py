def main():
    # main accepts no args
    # Calls all functions to play the number of games specified
    pass

def output_dice(dice):
    # Accepts dice
    # Outputs each dice in the list to the console
    pass

def roll_die():
    # Accepts no arguments
    # Returns a random integer from 1 to 6
    pass

def first_roll():
    # Accepts no arguments
    # Uses roll_die to generate a list of 12 integers
    # Returns a list of 12 random integers
    pass

def count_frequency(dice, target_number):
    # Accepts a list of 12 random integers and a target value
    # Returns how often that target value occurs in the list
    count = 0
    
    for die in dice:
        if die == target_number:
           count += 1
    print(count)

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
            mode = die
    print(mode)

def list_unmatched_dice(dice):
    # Accepts a list of dice
    # Determines which dice need rerolled
    # Returns a list of indexes to reroll
    pass

def reroll_one(dice, index):
    # Accepts a list of dice and an index.
    # Uses roll_die to reroll that index
    # Returns a new list with that index rerolled
    pass

def reroll_many(dice):
    # Accepts a list of dice
    # Calls list_unmatched_dice() and reroll_one() to reroll each die != the mode.
    # Returns a list of rerolled dice.
    pass







# Task: https://exercism.org/tracks/python/exercises/grains

TOTAL_NUMBER_OF_SQUARES = 64

def square(number):
    if __number_check(number):
        return 2 ** (number - 1)
        
def total():
    return 2 ** TOTAL_NUMBER_OF_SQUARES - 1

def __number_check(number):
    if type(number) != type(1):
        raise TypeError("You must enter a interger number")
    elif number < 1:
        raise ValueError("square must be between 1 and 64")
    elif number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return True
        
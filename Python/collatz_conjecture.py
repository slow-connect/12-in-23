# Task: https://exercism.org/tracks/python/exercises/collatz-conjecture

def steps(number):
    if type(number) != type(1):
        raise ValueError("Only integers are allowed")
    elif number < 1:
        raise ValueError("Only positive integers are allowed")
    else:
        counter = 0
        while number != 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = 3* number + 1
            counter +=1
    return counter


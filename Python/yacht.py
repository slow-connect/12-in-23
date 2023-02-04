# Task:  https://exercism.org/tracks/python/exercises/yacht/edit
# Score categories.
# Change the values as you see fit.
YACHT = "Yacht"
ONES = '1'
TWOS = '2'
THREES = '3'
FOURS = '4'
FIVES = '5'
SIXES = '6'
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four_of_kind"
LITTLE_STRAIGHT = "little"
BIG_STRAIGHT =  "big"
CHOICE = "choise"


def score(dice, category):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for i in range(5):
        if dice[i] == 1:
            one += 1
        elif dice[i] == 2:
            two += 1
        elif dice[i] == 3:
            three += 1
        elif dice[i] == 4:
            four += 1
        elif dice[i] == 5:
            five += 1
        elif dice[i] == 6:
            six += 1
    dices = [one, two, three, four, five, six]
    if category == YACHT:
        if any(val == 5 for val in dices):
            return 50
        else: 
            return 0
    elif category == CHOICE:
        return sumd(dices)
    elif len(category) == 1:
        return int(category) * dices[int(category) - 1]
    elif category == FULL_HOUSE:
        if any(val == 3 for val in dices) and any(val == 2 for val in dices):
            return sumd(dices)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        if any(val >= 4 for val in dices):
            return 4* (dices.index(max(dices)) + 1)
        else: return 0
    elif category == LITTLE_STRAIGHT or category == BIG_STRAIGHT:
        if all(val < 2 for val in dices):
            if category == LITTLE_STRAIGHT:
                if dices[-1] == 0:
                    return 30
                else: return 0
            else: 
                if dices[0] == 0:
                    return 30
                else: return 0
        else: return 0
        
    
def sumd(dices):
    sum = 0
    for i in range(len(dices)):
        sum += (i + 1) * dices[i]
    return sum
    

print(score([2, 2, 4, 4, 4], FULL_HOUSE))

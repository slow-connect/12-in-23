# Task: https://exercism.org/tracks/python/exercises/armstrong-numbers
def is_armstrong_number(number):
    if not number >= 0:
        raise ValueError("Only positive integer allowed")
    else:
        str_num = str(number)
        length = len(str_num)
        copy = number
        res = 0
        while copy != 0:
            rest = copy % 10
            res += rest ** length
            copy = copy // 10
        if res == number:
            return True
        else:
            return False

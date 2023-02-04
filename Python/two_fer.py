# Task: https://exercism.org/tracks/python/exercises/two-fer

def two_fer(*args):
    if len(args) == 0:
        print("One for you, one for me.")
    else:
        print("One for %s, one for me." % args[0])
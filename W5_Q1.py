import random
import time

craps = set([2, 3, 12])
naturals = set([7, 11])

random.seed(round(time.time() / 3, -1))  # do not seed elsewhere in your code


def roll_two_dices():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a, b


def print_lose():  # Write here
    print "You lose"
    return


def print_win():  # Write here
    print "You win"
    return


def print_point(p):  # Write here
    print "Your points are %d" % p
    return


def is_craps(n):  # Write here
    if n in craps:
        return True
    else:
        return False


def is_naturals(n):  # Write here
    if n in naturals:
        return True
    else:
        return False


def play_craps():
    point = -1
    while True:
        n1, n2 = roll_two_dices()
        sumn = n1 + n2
        print 'You rolled %d + %d = %d' % (n1, n2, sumn)
        if point == -1:
            if is_craps(sumn):
                print_lose()
                return 0
            elif is_naturals(sumn):
                print_win()
                return 1
            point = sumn
            print_point(point)
        else:
            if sumn == 7:
                print_lose()
                return 0
            elif sumn == point:
                print_win()
                return 1


play_craps()

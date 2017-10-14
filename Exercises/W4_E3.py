import random
import time

random.seed(round(time.time() / 3, -1))  # do not seed elsewhere in your code


def throw_dice(n, nExp):
    count = 0
    for i in range(nExp):
        check = False
        for j in range(n):
            if 6 == random.randint(1, 6):
                check = True
                break
        if check == True:
            count += 1
    print count
    return round(count / float(nExp), 2)

print throw_dice(1,100000)
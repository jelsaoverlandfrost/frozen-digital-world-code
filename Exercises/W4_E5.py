#### name your function game
import math
import random
import time

random.seed(round(time.time() / 3, -1))  # do not seed elsewhere in your code


def game(r, N):
    count = 0
    for j in range(N):
        summation = 0
        for i in range(0, 4):
            summation = summation + random.randint(1, 6)
        if summation < 9:
            count += 1
    profit = r * count - N
    if profit >= 0:
        return True
    else:
        return False

print game(10,1000)
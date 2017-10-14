import math
import random
import time

random.seed(round(time.time() / 3, -1))  # do not seed elsewhere in your code


def pi_approx_by_monte_carlo(numThrows):
    count = 0
    for i in range(numThrows):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1.0 * 1.0:
            count += 1
    pi = 4.0 * count / float(numThrows)
    return round(pi, 2)

print pi_approx_by_monte_carlo(10000)
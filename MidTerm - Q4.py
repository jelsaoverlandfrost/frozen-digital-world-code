#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.
import types

def mysum(a, b, limit):
    final_sum = 0
    start = 0
    if a <= 0 or b <= 0:
        return 'Wrong input'
    elif type(a) is not types.IntType or type(b) is not types.IntType:
        return 'Wrong input'
    else:
        if a > b:
            start = b
        else:
            start = a
        for i in range(start, limit):
            if i % a == 0 or i % b == 0:
                final_sum += i
    return final_sum


print mysum(21,34,10000)

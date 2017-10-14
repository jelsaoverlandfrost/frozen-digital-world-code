#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def num_of_sol(n):
    count = 0
    a = n
    while a >= 0:
        for b in range(0, n-a+1):
            for c in range(0, n-a-b+1):
                for d in range(0, n-a-b-c+1):
                    for e in range(0, n-a-b-c-d+1):
                        if a + b + c + d + e == n:
                            count += 1
                            break
        a -= 1
    return count


print num_of_sol(150)
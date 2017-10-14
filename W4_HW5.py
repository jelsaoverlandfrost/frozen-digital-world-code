def diff(p):
    dp = {}
    for j in p:
        if j != 0:
            dp[j - 1] = j * p[j]
        else:
            continue
    return dp


p = {1:-3, 3:2, 5:-1, 6:2}
print diff(p)
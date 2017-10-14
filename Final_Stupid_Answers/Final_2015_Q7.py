def countNumOpenLocker(K):
    # Initializing the lockers
    lockers = ['c'] * K
    times = 0
    while times <= K:
        if times == 0:
            times += 1
            continue
        else:
            for i in range(times, K+1, times):
                # print i
                if lockers[i-1] == 'o':
                    lockers[i-1] = 'c'
                else:
                    lockers[i-1] = 'o'
            times += 1
    counts = 0
    for i in lockers:
        if i == 'o':
            counts += 1
    return counts


print countNumOpenLocker(6)
print countNumOpenLocker(10)
print countNumOpenLocker(20)
print countNumOpenLocker(2000)

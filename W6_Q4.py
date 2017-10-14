class Coordinate:
    x = 0
    y = 0


import math


def get_maxmin_mag(f):
    lines = f.readlines()
    magmax = -100
    magmin = 100
    pmaxx = 0.0
    pmaxy = 0.0
    pminx = 0.0
    pminy = 0.0
    for i in lines:
        split = i.split()
        pair = Coordinate()
        pair.x = float(split[0])
        pair.y = float(split[1])
        mag = math.sqrt(pair.x ** 2 + pair.y ** 2)
        if mag > magmax:
            magmax = mag
            pmaxx = pair.x
            pmaxy = pair.y
        elif mag < magmin:
            magmin = mag
            pminx = pair.x
            pminy = pair.y

    max_pair = Coordinate()
    max_pair.x = pmaxx
    max_pair.y = pmaxy

    min_pair = Coordinate()
    min_pair.x = pminx
    min_pair.y = pminy

    return max_pair, min_pair

f = open('xy.dat','r')
pmax, pmin = get_maxmin_mag(f)
print 'max:(%f, %f)'%(pmax.x, pmax.y)
print 'min:(%f, %f)'%(pmin.x, pmin.y)

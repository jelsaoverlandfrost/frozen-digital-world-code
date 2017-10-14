from math import pi


def vol_cylinder(radius, length):
    area = radius * radius * pi
    volume = area * length
    return (area, volume)


import W2_HW2

print W2_HW2.vol_cylinder(1, 1)

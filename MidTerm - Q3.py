#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

import math


def area_r_polygon(n, s):
    area = n * (s ** 2) / (4.0 * math.tan(math.pi / n))
    return round(area, 3)
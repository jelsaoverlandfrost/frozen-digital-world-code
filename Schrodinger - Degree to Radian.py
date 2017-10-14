import scipy.constants as c


def degToRad(n):
    deg = float((c.pi / 180) * n)
    deg = round(deg, 5)
    return deg


def radToDeg(n):
    rad = float((180 / c.pi) * n)
    rad = round(rad, 5)
    return rad
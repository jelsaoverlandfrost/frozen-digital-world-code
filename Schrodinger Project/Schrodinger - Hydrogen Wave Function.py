import numpy as np
import scipy.constants as c
import math
import cmath


def cartesianToSpherical(x, y, z):
    x = float(x)
    y = float(y)
    z = float(z)
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    if x != 0:
        phi = np.arctan(y / x)
    else:
        ep = 1e-20
        phi = np.arctan(y / ep)
    theta = np.arccos(z / r)
    r = round(r, 5)
    phi = round(phi, 5)
    theta = round(theta, 5)
    return r, theta, phi


def radial_wave_func(n, l, r):
    a = c.physical_constants['Bohr radius'][0]
    p = (2 * l) + 1
    qmp = n - l - 1
    x = (2.0 * r) / (n * a)
    lfunc = assoc_laguerre(p, qmp)
    y = lfunc(x)
    b = (2.0 / (n * a)) ** 3
    d = (math.factorial(n - l - 1.0)) / (2.0 * n * (math.factorial(n + l)) ** 3)
    f = math.e ** (-r / (n * a))
    g = (2.0 * r / (n * a)) ** l
    wf = math.sqrt(b * d) * f * g * y
    return np.round(wf / (a ** -1.5), 5)


# for legendre
def p00(theta):
    return 1


def p01(theta):
    return np.cos(theta)


def p02(theta):
    return 0.5 * (3 * np.cos(theta) ** 2 - 1)


def p03(theta):
    return 0.5 * (5 * np.cos(theta) ** 3 - 3 * np.cos(theta))


def p11(theta):
    return np.sin(theta)


def p12(theta):
    return 3 * np.sin(theta) * np.cos(theta)


def p13(theta):
    return 1.5 * np.sin(theta) * (5 * np.cos(theta) ** 2 - 1)


def p22(theta):
    return 3 * np.sin(theta) ** 2


def p23(theta):
    return 15 * np.sin(theta) ** 2 * np.cos(theta)


def p33(theta):
    return 15 * np.sin(theta) * (1 - np.cos(theta) ** 2)


def assoc_legendre(m, l):
    if m == 0 and l == 0:
        return p00
    elif m == 0 and l == 2:
        return p02
    elif m == 1 and l == 1:
        return p11
    elif m == -1 and l == 1:
        return p11
    elif m == 3 and l == 3:
        return p33
    elif m == -3 and l == 3:
        return p33
    elif m == 0 and l == 1:
        return p01
    elif m == 2 and l == 3:
        return p23
    elif m == -2 and l == 3:
        return p23
    elif m == 2 and l == 2:
        return p22
    elif m == -2 and l == 2:
        return p22
    elif m == 1 and l == 3:
        return p13
    elif m == -1 and l == 3:
        return p13
    elif m == 1 and l == 2:
        return p12
    elif m == -1 and l == 2:
        return p12
    elif m == 0 and l == 3:
        return p03
    else:
        return None


###For laguerre from model ans
def l00(x):
    return 1


def l01(x):
    return -x + 1


def l02(x):
    return x * x - 4 * x + 2


def l10(x):
    return 1


def l11(x):
    return -2 * x + 4


def l12(x):
    return 3 * x * x - 18 * x + 18


def l13(x):
    return -4 * x * x * x + 48 * x * x - 144 * x + 96


def l20(x):
    return 2


def l21(x):
    return -6 * x + 18


def l23(x):
    return -20 * x * x * x + 300 * x * x - 1200 * x + 1200


def l22(x):
    return 12 * x * x - 96 * x + 144


def l03(x):
    return -x * x * x + 9 * x * x - 18 * x + 6


def l30(x):
    return 6


def l31(x):
    return -24 * x + 96


def l32(x):
    return 60 * x * x - 600 * x + 1200


def l33(x):
    return -120 * x * x * x - 10800 * x + 2160 * x * x + 14400


def l51(x):
    return -720 * x + 4320


def l70(x):
    return -5040


def assoc_laguerre(p, qmp):
    if p == 0 and qmp == 0:
        return l00
    elif p == 0 and qmp == 1:
        return l01
    elif p == 0 and qmp == 2:
        return l02
    elif p == 0 and qmp == 3:
        return l03
    elif p == 1 and qmp == 0:
        return l10
    elif p == 1 and qmp == 1:
        return l11
    elif p == 1 and qmp == 2:
        return l12
    elif p == 1 and qmp == 3:
        return l13
    elif p == 2 and qmp == 0:
        return l20
    elif p == 2 and qmp == 1:
        return l21
    elif p == 2 and qmp == 2:
        return l22
    elif p == 2 and qmp == 3:
        return l23
    elif p == 3 and qmp == 0:
        return l30
    elif p == 3 and qmp == 1:
        return l31
    elif p == 3 and qmp == 2:
        return l32
    elif p == 3 and qmp == 3:
        return l33
    elif p == 5 and qmp == 1:
        return l51
    elif p == 7 and qmp == 0:
        return l70
    else:
        return None


def angular_wave_func(m, l, theta, phi):
    pfunc = assoc_legendre(m, l)
    y = pfunc(theta)

    if m > 0:
        a = float(2 * l + 1) / (4 * np.pi)
        b = float(math.factorial(l - abs(m))) / math.factorial(l + abs(m))
        i = cmath.sqrt(-1)
        d = math.e ** (i * m * phi)
        wf = ((-1) ** m) * math.sqrt(a * b) * d * y
        return np.around(wf, 5)

    if m <= 0:
        a = float(2 * l + 1) / (4 * np.pi)
        b = float(math.factorial(l - abs(m))) / math.factorial(l + abs(m))
        i = cmath.sqrt(-1)
        d = math.e ** (i * m * phi)
        wf = math.sqrt(a * b) * d * y
        return np.around(wf, 5)


# Hydrogen Wave function

def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    x = np.round(np.linspace(-roa, roa, Nx), 5)
    y = np.round(np.linspace(-roa, roa, Ny), 5)
    z = np.round(np.linspace(-roa, roa, Nz), 5)
    xx, yy, zz = np.meshgrid(x, y, z)
    print 'a'
    a = c.physical_constants['Bohr radius'][0]
    carToSphere_v = np.vectorize(cartesianToSpherical)
    r, theta, phi = carToSphere_v(xx, yy, zz)
    radialWavef_v = np.vectorize(radial_wave_func)
    print 'r'
    rad = radialWavef_v(n, l, r * a)
    if m >=0 :
        angular = (1/np.sqrt(2)) * (np.vectorize(angular_wave_func)(m,l,theta,phi) + np.vectorize(angular_wave_func)(-m,l,theta,phi) )
    else:
        angular = (-1/np.sqrt(2)) * (np.vectorize(angular_wave_func)(m,l,theta,phi) - np.vectorize(angular_wave_func)(-m,l,theta,phi) )

    magnitude = (rad * angular) ** 2
    magnitude = np.absolute(magnitude)
    magnitude = np.round(magnitude, 5)

    return xx, yy, zz, magnitude


# print 'Test 1'
# x, y, z, mag = hydrogen_wave_func(2, 1, 1, 8, 2, 2, 2)
# print 'x,y,z:'
# print x, y, z
# print 'mag:'
# print mag
#
# print 'Test 2'
# x, y, z, mag = hydrogen_wave_func(2, 1, 1, 5, 3, 4, 2)
# print 'x,y,z:'
# print x, y, z
# print 'mag:'
# print mag
#
x, y, z, mag = hydrogen_wave_func(4, 0, 0, 20, 50, 50, 50)
x.dump('xdata400.dat')
y.dump('ydata400.dat')
z.dump('zdata400.dat')
mag.dump('density400.dat')

x, y, z, mag = hydrogen_wave_func(4, 1, 0, 30, 50, 50, 50)
x.dump('xdata410.dat')
y.dump('ydata410.dat')
z.dump('zdata410.dat')
mag.dump('density410.dat')

x, y, z, mag = hydrogen_wave_func(4, 1, 1, 30, 50, 50, 50)
x.dump('xdata411.dat')
y.dump('ydata411.dat')
z.dump('zdata411.dat')
mag.dump('density411.dat')

x, y, z, mag = hydrogen_wave_func(4, 1, -1, 30, 50, 50, 50)
x.dump('xdata41-1.dat')
y.dump('ydata41-1.dat')
z.dump('zdata41-1.dat')
mag.dump('density41-1.dat')

x, y, z, mag = hydrogen_wave_func(4, 2, 0, 30, 50, 50, 50)
x.dump('xdata420.dat')
y.dump('ydata420.dat')
z.dump('zdata420.dat')
mag.dump('density420.dat')

x, y, z, mag = hydrogen_wave_func(4, 2, 1, 30, 50, 50, 50)
x.dump('xdata421.dat')
y.dump('ydata421.dat')
z.dump('zdata421.dat')
mag.dump('density421.dat')

x, y, z, mag = hydrogen_wave_func(4, 2, -1, 30, 50, 50, 50)
x.dump('xdata42-1.dat')
y.dump('ydata42-1.dat')
z.dump('zdata42-1.dat')
mag.dump('density42-1.dat')

x, y, z, mag = hydrogen_wave_func(4, 2, 2, 30, 50, 50, 50)
x.dump('xdata422.dat')
y.dump('ydata422.dat')
z.dump('zdata422.dat')
mag.dump('density422.dat')

x, y, z, mag = hydrogen_wave_func(4, 2, -2, 30, 50, 50, 50)
x.dump('xdata42-2.dat')
y.dump('ydata42-2.dat')
z.dump('zdata42-2.dat')
mag.dump('density42-2.dat')

x, y, z, mag = hydrogen_wave_func(4, 3, 0, 30, 50, 50, 50)
x.dump('xdata430.dat')
y.dump('ydata430.dat')
z.dump('zdata430.dat')
mag.dump('density430.dat')

x, y, z, mag = hydrogen_wave_func(4, 3, 1, 30, 50, 50, 50)
x.dump('xdata431.dat')
y.dump('ydata431.dat')
z.dump('zdata431.dat')
mag.dump('density431.dat')

x, y, z, mag = hydrogen_wave_func(4, 3, -1, 30, 50, 50, 50)
x.dump('xdata43-1.dat')
y.dump('ydata43-1.dat')
z.dump('zdata43-1.dat')
mag.dump('density43-1.dat')

x, y, z, mag = hydrogen_wave_func(4, 3, 2, 30, 50, 50, 50)
x.dump('xdata432.dat')
y.dump('ydata432.dat')
z.dump('zdata432.dat')
mag.dump('density432.dat')

x, y, z, mag = hydrogen_wave_func(4, 3, -2, 30, 50, 50, 50)
x.dump('xdata43-2.dat')
y.dump('ydata43-2.dat')
z.dump('zdata43-2.dat')
mag.dump('density43-2.dat')

x, y, z, mag = hydrogen_wave_func(4, 3, 3, 30, 50, 50, 50)
x.dump('xdata433.dat')
y.dump('ydata433.dat')
z.dump('zdata433.dat')
mag.dump('density433.dat')

x, y, z, mag = hydrogen_wave_func(4, 3, -3, 30, 50, 50, 50)
x.dump('xdata43-3.dat')
y.dump('ydata43-3.dat')
z.dump('zdata43-3.dat')
mag.dump('density43-3.dat')
def l00(x):
    return 1


def l01(x):
    return -x + 1


def l02(x):
    return x * x - 4 * x + 2


def l03(x):
    return x ** 3 + 9 * x * x - 18 * x + 6


def l10(x):
    return 1


def l11(x):
    return - 2 * x + 4


def l12(x):
    return -3 * x * x - 18 * x + 18


def l13(x):
    return -4 * x * x * x + 9 * x * x - 18 * x + 6


def l20(x):
    return 2


def l21(x):
    return 6 * x + 18


def l22(x):
    return 12 * x * x - 16 * x + 144


def l23(x):
    return 20 * x * x * x - 300 * x * x - 1200 * x + 1200


def l30(x):
    return 6


def l31(x):
    return -24 * x + 96


def l32(x):
    return 60 * x * x + 600 * x + 1200


def l33(x):
    return -120 * x * x * x - 10800 * x + 2160 * x * x + 14400


def assoc_laguerre(p, qmp):
    if p == 0:
        if qmp == 0:
            return l00
        elif qmp == 1:
            return l01
        elif qmp == 2:
            return l02
        elif qmp == 3:
            return l03
    if p == 1:
        if qmp == 0:
            return l10
        elif qmp == 1:
            return l11
        elif qmp == 2:
            return l12
        elif qmp == 3:
            return l13
    if p == 2:
        if qmp == 0:
            return l20
        elif qmp == 1:
            return l21
        elif qmp == 2:
            return l22
        elif qmp == 3:
            return l23
    if p == 3:
        if qmp == 0:
            return l30
        elif qmp == 1:
            return l31
        elif qmp == 2:
            return l32
        elif qmp == 3:
            return l33

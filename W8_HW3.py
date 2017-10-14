from math import *


# return only the derivative value without rounding
# your return value is a float, which is the approximate value of the derivative
# Tutor will compute the approximate error based on your return value

class Diff:
    def __init__(self, f, h=1E-4):
        self.h = h
        self.function = f

    def __call__(self, x):
        return (self.function(x + self.h) - self.function(x)) / self.h


def f(x):
    return 0.25 * x ** 4


df = Diff(f)

for x in (1, 5, 10):
    df_value = df(x)  # approx value of derivative of f at point x
    exact = x ** 3  # exact value of derivative
    print "f '(%d)=%g(error=%.2E)" % (x, df_value, exact - df_value)

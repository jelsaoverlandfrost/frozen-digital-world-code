from math import *


class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def __call__(self, x):
        return exp(-self.a * x) * sin(self.w * x)

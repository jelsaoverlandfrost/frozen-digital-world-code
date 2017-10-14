import math


class QuadraticEquation(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_roots(self):
        if self.b ** 2 - (4 * self.a * self.c) >= 0:
            delta = math.sqrt(self.b ** 2 - (4 * self.a * self.c))
            return (-self.b - delta) / 2 * self.a, (-self.b + delta) / 2 * self.a
        else:
            return 'No real roots'

    def __str__(self):
        if self.a == 1:
            if self.b == 1:
                return 'f(x) = x^2 + x + %d' % self.c
            elif self.b == 0:
                return 'f(x) = x^2 + %d' % self.c
            else:
                return 'f(x) = x^2 + %dx + %d' % (self.b, self.c)
        else:
            if self.b == 1:
                return 'f(x) = x^2 + x + %d' % self.c
            elif self.b == 0:
                return 'f(x) = x^2 + %d' % self.c
            else:
                return 'f(x) = x^2 + %dx + %d' % (self.b, self.c)

    def __eq__(self, other):
        return (self.a == other.a) and (self.b == other.b) and (self.b == other.b)

    def __call__(self, x):
        return self.a * (x ** 2) + self.b * x + self.c


f = QuadraticEquation(1, 5, 4)
print f(0)
print f
print f.get_roots()
g = QuadraticEquation(1, 5, -4)
print f == g

class Polynomial(object):
    def __init__(self, polynomial_list):
        self.coeff = polynomial_list

    def __call__(self, x):
        final_value = 0
        for i in range(len(self.coeff)):
            final_value += self.coeff[i] * (x ** i)
        return final_value

    def __add__(self, other):
        a = []
        if len(self.coeff) <= len(other.coeff):
            for i in range(len(self.coeff)):
                a.append(self.coeff[i] + other.coeff[i])
            for i in range(len(self.coeff), len(other.coeff)):
                a.append(other.coeff[i])
        else:
            for i in range(len(other.coeff)):
                a.append(self.coeff[i] + other.coeff[i])
        return Polynomial(a)

    def __sub__(self, other):
        a = []
        if len(self.coeff) >= len(other.coeff):
            for i in range(len(other.coeff)):
                a.append(self.coeff[i] - other.coeff[i])
            for i in range(len(other.coeff), len(self.coeff)):
                a.append(self.coeff[i])
        else:
            for i in range(len(self.coeff)):
                a.append(self.coeff[i] - other.coeff[i])
            for i in range(len(self.coeff), len(other.coeff)):
                a.append(-other.coeff[i])
        return Polynomial(a)

    def __mul__(self, other):
        a = [0] * (len(self.coeff) + len(other.coeff))
        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                a[i + j] += self.coeff[i] * other.coeff[j]
        k = len(a) - 1
        while k >= 0:
            if a[k] == 0:
                del a[k]
                k -= 1
            else:
                break
        return Polynomial(a)

    def differentiate(self):
        for i in range(1, len(self.coeff)):
            self.coeff[i] *= i
        del self.coeff[0]

    def derivative(self):
        a = []
        for i in range(1, len(self.coeff)):
            n = self.coeff[i] * i
            a.append(n)
        return Polynomial(a)


p1 = Polynomial([1, -1, 9, 0, 6])
p2 = Polynomial([0, 1, 0, 0, -6, -1])
p3 = p1 + p2
print p3.coeff
p4 = p1 * p2
print p4.coeff
p1.differentiate()
print p1.coeff
p = Polynomial([1, 2, 3])
q = Polynomial([2, 3])
r = p - q
print r.coeff
r = q - p
print r.coeff

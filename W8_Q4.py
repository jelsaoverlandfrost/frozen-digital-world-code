class Line(object):
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        return round(self.c1 * x + self.c0, 2)

    def table(self, L, R, n):
        if n <= 0:
            return 'Error in printing table'
        elif L == R:
            return '%10.2f%10.2f\n' % (L, self(L))
        else:
            final_string = ''
            initial = L
            for i in range(n):
                final_string += '%10.2f%10.2f\n' % (initial, self(initial))
                initial += (R - L) / float(n - 1)
            return final_string


line = Line(3, 4)
print line(2)
print line.table(1, 1, 15)

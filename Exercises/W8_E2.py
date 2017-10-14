class Line0(object):
    def __init__(self, A, B):
        x1, y1 = A
        x2, y2 = B
        if x1 == x2:
            self.b = 0
            self.a = 1
            self.c = 0 - x1
        elif y1 == y2:
            self.a = 0
            self.b = 1
            self.c = 0 - y1
        else:
            self.a = 1
            self.b = float(x2 - x1) / (y1 - y2)
            self.c = 0 - (x1 + self.b * y1)

    def __call__(self, x):
        return float(0 - self.c - self.a * x) / self.b

import better_exceptions
class Square(object):
    def __init__(self, x=0, y=0, sideLength=1.0):
        self.x = x
        self.y = y
        self.sideLength = sideLength

    def getCenter(self):
        return self.x, self.y

    def getSideLength(self):
        return self.sideLength

    def getArea(self):
        return self.sideLength ** 2

    def getPerimeter(self):
        return self.sideLength * 4

    def containPoint(self, px, py):
        checker = False
        if (self.x - self.sideLength / 2) <= px <= (self.x + self.sideLength / 2):
            if (self.y - self.sideLength / 2) <= py <= (self.y + self.sideLength / 2):
                checker = True
        return checker

    def containSquare(self, inSquare):
        checker = False
        if inSquare.x + inSquare.sideLength / 2 <= (self.x + self.sideLength / 2):
            if inSquare.x - inSquare.sideLength / 2 >= (self.x - self.sideLength / 2):
                if inSquare.y + inSquare.sideLength / 2 <= (self.y + self.sideLength / 2):
                    if inSquare.y - inSquare.sideLength / 2 >= (self.y - self.sideLength / 2):
                        checker = True
        return checker


s = Square(x=1, y=1, sideLength=2.0)
print s.getCenter()
print s.getSideLength()
print s.getArea()
print s.getPerimeter()
print s.containPoint(0, 0)
print s.containPoint(0, -0.5)
print s.containPoint(1, 1.5)
print s.containSquare(Square(x=1.5, y=1, sideLength=1))
print s.containSquare(Square(x=1.5, y=1, sideLength=1.1))
s2 = Square()
print s2.getCenter()
print s2.getSideLength()
print s2.getPerimeter()

import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point2D(' + str(self.x) + ',' + str(self.y) + ')'

    def add(self, vector):
        x = self.x + vector.dx
        y = self.y + vector.dy
        return Point2D(x, y)


class Vector2D:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def length(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)


class Polyline2D:
    def __init__(self, startPoint, listOfVectors):
        self.startPoint = startPoint
        self.listOfVector = listOfVectors

    def addSegment(self, Vector):
        self.listOfVector.append(Vector)

    def length(self):
        length = 0
        for i in self.listOfVector:
            length += i.length()
        return length

    def vertex(self, vertexNumber):
        self.vertexCoordinate = self.startPoint
        for i in range(0, vertexNumber):
            self.vertexCoordinate = self.vertexCoordinate.add(self.listOfVector[i])
        return self.vertexCoordinate


class ClosedPolyline2D(Polyline2D):
    def length(self):
        length = 0
        for i in self.listOfVector:
            length += i.length()
        self.vertexCoordinate = self.startPoint
        for i in range(0, len(self.listOfVector)):
            self.vertexCoordinate = self.vertexCoordinate.add(self.listOfVector[i])
        finalVector = Vector2D(self.startPoint.x - self.vertexCoordinate.x,
                               self.startPoint.y - self.vertexCoordinate.y)
        length += finalVector.length()
        return length


pline = Polyline2D(Point2D(1, 2), [Vector2D(3, 1)])
pline.addSegment(Vector2D(1, 0))
pline.addSegment(Vector2D(0, 2))
print pline.length()
print pline.vertex(0)
print pline.vertex(1)
print pline.vertex(2)
print pline.vertex(3)
cpline = ClosedPolyline2D(Point2D(1, 2), [Vector2D(3, 1)])
cpline.addSegment(Vector2D(1, 0))
cpline.addSegment(Vector2D(0, 2))
print cpline.length()

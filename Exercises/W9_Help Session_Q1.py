class Rectangle:
    def __init__(self, width=1, height=2):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        if width >= 0:
            self._width = width
        else:
            self._width = -width

    def get_width(self):
        return self._width

    def set_height(self, height):
        if height >= 0:
            self._height = height
        else:
            self._height = -height

    def get_height(self):
        return self._height

    def get_area(self):
        return self._height * self._width

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def __eq__(self, other):
        return (self._height == other._height) and (self._width == other._width)

    def __str__(self):
        return 'rectangle has width %.2f nd height %.2f' % (self._width, self._height)

    width = property(get_width, set_width)
    height = property(get_height, set_height)


R1 = Rectangle()
R2 = Rectangle(1, 2)
R3 = Rectangle(-1, 2)
print R1.width
print R2.width
print R3.width
print R1 == R2
print R1
R3.width = 5
print R1.get_area()
print R2.get_area()
print R3.get_area()

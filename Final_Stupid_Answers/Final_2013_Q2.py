# Another choice is to declare an Global Variable here
# count = 0


# Visitor class
class Visitor(object):
    # A variable to count the number of calls for a visitor
    callCount = 0

    # Piazza! This is a property of the Class Visitor
    count = 0

    # Initialization
    def __init__(self, name='Visitor'):
        Visitor.count += 1
        if name != 'Visitor':
            self.name = name
        else:
            self.name = name + ' ' + str(Visitor.count)

    def setName(self, name):
        self.name = name

    def __call__(self):
        self.callCount += 1
        return self.name + ' called the ' + str(self.callCount) + 'th time'


v1 = Visitor('John')
print v1()
v2 = Visitor()
print v2()
print v1()
v2.setName('Marina')
print v2()
v3 = Visitor()
print v3()

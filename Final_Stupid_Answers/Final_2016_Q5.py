class Avatar(object):
    def __init__(self, name, hp=100, position=(1, 1)):
        self.name = name
        self.hp = hp
        self.position = position

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getHP(self):
        return self.hp

    def setHP(self, hp):
        self.hp = hp

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def heal(self, healingVal=1):
        if healingVal >= 0:
            self.hp += healingVal

    def attacked(self, attackVal=-1):
        if attackVal <= 0:
            self.hp += attackVal

# Test cases
print 'test 1: __init__'
a = Avatar('John')
print (a.name, a.hp, a.position)
print 'test 2: __init__'
a = Avatar('Jane', 150, (10, 10))
print (a.name, a.hp, a.position)
print 'test 3: getName(), setName()'
a = Avatar('John')
a.setName('Jude')
print a.getName()
print 'test 4: getPosition(), setPosition()'
a = Avatar('John')
a.setPosition((1, 3))
print a.getPosition()
print 'test 5: getHP(), setHP()'
a = Avatar('John')
a.setHP(200)
print a.getHP()
print 'test 6: heal()'
a = Avatar('John')
a.heal(5)
print a.getHP()
print 'test 7: attacked()'
a = Avatar('John')
a.attacked(20)
print a.getHP()
print 'test 8: heal()'
a = Avatar('John')
a.heal()
print a.getHP()
print 'test 9: attacked()'
a = Avatar('John')
a.attacked()
print a.getHP()
print 'test 10: heal(), attacked() '
a = Avatar('John')
a.attacked(2)
a.heal(-2)
print a.getHP()

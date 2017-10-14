from libdw import sm
import copy


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


class Map(object):
    def __init__(self, mapInfo):
        self.world = copy.deepcopy(mapInfo)

    def whatIsAt(self, position):
        if position not in self.world.keys():
            return 'Empty'
        else:
            objectKind = self.world[position]
            if objectKind == 'x':
                return 'Exit'
            elif objectKind == 0:
                return 'Wall'
            elif objectKind > 0:
                return 'Food'
            elif objectKind < 0:
                return 'Enemy'

    def getEnemyAttack(self, position):
        if position in self.world.keys():
            if self.world[position] < 0:
                return self.world[position]
            else:
                return False
        else:
            return False

    def getFoodEnergy(self, position):
        if position in self.world.keys():
            if self.world[position] > 0:
                return self.world[position]
            else:
                return False
        else:
            return False

    def removeEnemy(self, position):
        if self.world[position] < 0:
            self.world.pop(position)
            return True
        else:
            return False

    def eatFood(self, position):
        if self.world[position] > 0:
            self.world.pop(position)
            return True
        else:
            return False

    def getExitPosition(self):
        if 'x' in self.world.values():
            return self.world.keys()[self.world.values().index('x')]
        else:
            return None


class DW2Game(sm.SM):
    def __init__(self, avatar, envmap):
        self.avatar = copy.deepcopy(avatar)
        self.map = copy.deepcopy(envmap)
        self.startState = self.avatar, self.map

    def getNextValues(self, state, inp):
        self.avatarUpdated = copy.deepcopy(state[0])
        self.mapUpdated = copy.deepcopy(state[1])
        if inp[0] == 'move':
            if inp[1] == 'up':
                objectiveForward = state[1].whatIsAt((state[0].getPosition()[0], state[0].getPosition()[1] - 1))
                if objectiveForward == 'Wall':
                    pass
                elif objectiveForward == 'Enemy':
                    enemyPosition = state[0].getPosition()[0], state[0].getPosition()[1] - 1
                    self.avatarUpdated.attacked(self.map.getEnemyAttack(enemyPosition))
                elif objectiveForward == 'Food':
                    newPosition = state[0].getPosition()[0], state[0].getPosition()[1] - 1
                    foodPosition = state[0].getPosition()[0], state[0].getPosition()[1] - 1
                    self.avatarUpdated.setPosition(newPosition)
                    self.avatarUpdated.heal(self.mapUpdated.getFoodEnergy(foodPosition))
                    self.mapUpdated.eatFood(foodPosition)
                else:
                    newPosition = state[0].getPosition()[0], state[0].getPosition()[1] - 1
                    self.avatarUpdated.setPosition(newPosition)
            elif inp[1] == 'down':
                objectiveForward = state[1].whatIsAt((state[0].getPosition()[0], state[0].getPosition()[1] + 1))
                if objectiveForward == 'Wall':
                    pass
                elif objectiveForward == 'Enemy':
                    enemyPosition = state[0].getPosition()[0], state[0].getPosition()[1] + 1
                    self.avatarUpdated.attacked(self.map.getEnemyAttack(enemyPosition))
                elif objectiveForward == 'Food':
                    newPosition = state[0].getPosition()[0], state[0].getPosition()[1] + 1
                    foodPosition = state[0].getPosition()[0], state[0].getPosition()[1] + 1
                    self.avatarUpdated.setPosition(newPosition)
                    self.avatarUpdated.heal(self.mapUpdated.getFoodEnergy(foodPosition))
                    self.mapUpdated.eatFood(foodPosition)
                else:
                    newPosition = state[0].getPosition()[0], state[0].getPosition()[1] + 1
                    self.avatarUpdated.setPosition(newPosition)
            elif inp[1] == 'left':
                objectiveForward = state[1].whatIsAt((state[0].getPosition()[0] - 1, state[0].getPosition()[1]))
                if objectiveForward == 'Wall':
                    pass
                elif objectiveForward == 'Enemy':
                    enemyPosition = state[0].getPosition()[0] - 1, state[0].getPosition()[1]
                    self.avatarUpdated.attacked(self.map.getEnemyAttack(enemyPosition))
                elif objectiveForward == 'Food':
                    newPosition = state[0].getPosition()[0] - 1, state[0].getPosition()[1]
                    foodPosition = state[0].getPosition()[0] - 1, state[0].getPosition()[1]
                    self.avatarUpdated.setPosition(newPosition)
                    self.avatarUpdated.heal(self.mapUpdated.getFoodEnergy(foodPosition))
                    self.mapUpdated = self.mapUpdated.eatFood(foodPosition)
                else:
                    newPosition = state[0].getPosition()[0] - 1, state[0].getPosition()[1]
                    self.avatarUpdated.setPosition(newPosition)
            elif inp[1] == 'right':
                objectiveForward = state[1].whatIsAt((state[0].getPosition()[0] + 1, state[0].getPosition()[1]))
                if objectiveForward == 'Wall':
                    pass
                elif objectiveForward == 'Enemy':
                    newPosition = state[0].getPosition()[0], state[0].getPosition()[1]
                    enemyPosition = state[0].getPosition()[0] + 1, state[0].getPosition()[1]
                    self.avatarUpdated.setPosition(newPosition)
                    self.avatarUpdated.heal(self.map.getEnemyAttack(enemyPosition))
                elif objectiveForward == 'Food':
                    newPosition = state[0].getPosition()[0] + 1, state[0].getPosition()[1]
                    foodPosition = state[0].getPosition()[0] + 1, state[0].getPosition()[1]
                    self.avatarUpdated.setPosition(newPosition)
                    self.avatarUpdated.heal(self.mapUpdated.getFoodEnergy(foodPosition))
                    self.mapUpdated.eatFood(foodPosition)
                else:
                    newPosition = state[0].getPosition()[0] + 1, state[0].getPosition()[1]
                    self.avatarUpdated.setPosition(newPosition)

        elif inp[0] == 'attack':
            if inp[1] == 'up':
                objectiveForward = state[1].whatIsAt((state[0].getPosition()[0], state[0].getPosition()[1] - 1))
                if objectiveForward == 'Enemy':
                    enemyPosition = state[0].getPosition()[0], state[0].getPosition()[1] - 1
                    self.mapUpdated.removeEnemy(enemyPosition)
            elif inp[1] == 'down':
                objectiveForward = state[1].whatIsAt((state[0].getPosition()[0], state[0].getPosition()[1] + 1))
                if objectiveForward == 'Enemy':
                    enemyPosition = state[0].getPosition()[0], state[0].getPosition()[1] + 1
                    self.mapUpdated.removeEnemy(enemyPosition)
            elif inp[1] == 'right':
                objectiveForward = state[1].whatIsAt((state[0].getPosition()[0] + 1, state[0].getPosition()[1]))
                if objectiveForward == 'Enemy':
                    enemyPosition = state[0].getPosition()[0] + 1, state[0].getPosition()[1]
                    self.mapUpdated.removeEnemy(enemyPosition)
            elif inp[1] == 'left':
                objectiveForward = state[1].whatIsAt((state[0].getPosition()[0] - 1, state[0].getPosition()[1]))
                if objectiveForward == 'Enemy':
                    enemyPosition = state[0].getPosition()[0] - 1, state[0].getPosition()[1]
                    self.mapUpdated.removeEnemy(enemyPosition)

        nextState = self.avatarUpdated, self.mapUpdated
        output = self.avatarUpdated.getName(), self.avatarUpdated.getPosition(), self.avatarUpdated.getHP()
        return nextState, output

    def done(self, state):
        currentPosition = state[0].getPosition()
        exitPosition = state[1].getExitPosition()
        return currentPosition == exitPosition

world2 = {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, (4, 0): 0,
          (5, 0): 0, (0, 1): 0, (5, 1): 0, (0, 2): 0, (1, 2): -2, (5, 2): 0,
          (0, 3): 0, (2, 3): 3, (5, 3): 0, (0, 4): 0, (5, 4): 0, (0, 5): 0,
          (1, 5): 0, (2, 5): 0, (3, 5): 0, (4, 5): 'x', (5, 5): 0, }
print 'test 1'
inp = [('move', 'down'), ('attack', 'down'), ('move', 'down'), (
    'move', 'down'),
       ('move', 'down'), ('move', 'right'), ('move', 'right'), ('move', 'right'), ('move', 'down'),
       ('move', 'down')]
av = Avatar('John')
m = Map(world2)
g = DW2Game(av, m)
print m.getExitPosition()
print g.transduce(inp)
print 'test 2'
inp = [('move', 'left'), ('move', 'right'), ('move', 'right'), ('move', 'right'),
       ('move', 'right'), ('move', 'down'), ('move', 'down'), ('move', 'down'),
       ('move', 'up')]
av = Avatar('John')
m = Map(world2)
g = DW2Game(av, m)
print g.transduce(inp)
print 'test 3'
inp = [('move', 'right'), ('move', 'right'), ('move', 'right'),
       ('move', 'down'), ('move', 'left'), ('move', 'left'), ('move', 'left'),
       ('attack', 'left'), ('move', 'left')]
av = Avatar('John')
m = Map(world2)
g = DW2Game(av, m)
print g.transduce(inp)
print 'test 4'
inp = [('move', 'right'), ('move', 'right'), ('move', 'right'),
       ('move', 'down'), ('move', 'left'), ('move', 'left'), ('move', 'left'),
       ('attack', 'left'), ('move', 'left'), ('move', 'left'), ('move', 'down'),
       ('move', 'right')]
av = Avatar('John')
m = Map(world2)
g = DW2Game(av, m)
print g.transduce(inp)
print 'test 5'
inp = [('move', 'right'), ('move', 'right'), ('move', 'right'),
       ('move', 'down'), ('move', 'left'), ('move', 'left'), ('move', 'left'),
       ('attack', 'left'), ('move', 'left'), ('move', 'left'), ('move', 'down'),
       ('move', 'right'), ('move', 'right'), ('move', 'right'), ('move', 'down'),
       ('move', 'down'), ('move', 'down')]
av = Avatar('John')
m = Map(world2)
g = DW2Game(av, m)
print g.transduce(inp)
print 'test 6'
av = Avatar('John')
m = Map(world2)
g = DW2Game(av, m)
g.start()
n, o = g.getNextValues(g.startState, ('move', 'right'))
ans = g.state[0].getPosition() == n[0].getPosition()
print ans, g.state[0].getPosition(), n[0].getPosition()

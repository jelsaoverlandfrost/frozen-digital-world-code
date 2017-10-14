import libdw.sm as sm


# Comblock class
class CombLock(sm.SM):
    # Initialization of the class
    def __init__(self, keyList):
        self.keyList = keyList

    # A Container for the trail values
    trailList = []

    # SM Class
    def getNextValues(self, state, inp):
        if inp == 0:
            output = 'locked'
        elif 1 <= inp <= 9:
            self.trailList.append(inp)
            output = 'locked'
        elif inp == -1:
            if self.keyList == self.trailList:
                output = "unlocked"
            else:
                output = 'locked'
            self.trailList = []
        return output, output


# Test Cases 1
lock = CombLock([1, 2, 5])
print lock.transduce([1, 2, 5, -1])
print lock.transduce([1, 0, 2, 5, -1])
print lock.transduce([3, 2, 5, -1])
print lock.transduce([1, 2, 5, -1, 1, 2, 5, -1])
print lock.transduce([3, 2, 5, -1, 1, 2, 5, -1])


# Global function
def mapT2P(x, y):
    if 0 <= x <= 3:
        if 0 <= y <= 3:
            return 1
        if 4 <= y <= 7:
            return 4
        if 8 <= y <= 11:
            return 7
    if 4 <= x <= 7:
        if 0 <= y <= 3:
            return 2
        if 4 <= y <= 7:
            return 5
        if 8 <= y <= 11:
            return 8
    if 8 <= x <= 11:
        if 0 <= y <= 3:
            return 3
        if 4 <= y <= 7:
            return 6
        if 8 <= y <= 11:
            return 9


# TouchMap Class
class TouchMap(sm.SM):
    startState = 0
    trialSequence = []

    def getNextValues(self, state, inp):
        (e, x, y) = inp
        if e == 'TouchDown':
            self.trialSequence.append(mapT2P(x, y))
            nextState = mapT2P(x, y)
            output = mapT2P(x, y)
        if e == 'TouchUp':
            self.trialSequence.append(-1)
            nextState = 0
            output = -1
        elif e == 'TouchUpdate':
            if mapT2P(x, y) == state:
                self.trialSequence.append(0)
                nextState = state
                output = 0
            else:
                self.trialSequence.append(mapT2P(x, y))
                nextState = mapT2P(x, y)
                output = mapT2P(x, y)
        return nextState, output


# TouchMap Test Cases
m = TouchMap()
print m.transduce([('TouchDown', 2, 2), ('TouchUpdate', 3, 3), ('TouchUp', 4, 4)])
print m.transduce([('TouchDown', 3, 3), ('TouchUpdate', 4, 3), ('TouchUp', 4, 4)])

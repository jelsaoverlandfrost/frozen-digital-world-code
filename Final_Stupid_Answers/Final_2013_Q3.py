from libdw import sm


# From the problem description
class Fruit:
    def relativeMovement(self):
        return self.relativeRotation, self.unitsForward


class Apple(Fruit):
    relativeRotation = 0
    unitsForward = 1


class Pear(Fruit):
    relativeRotation = -90
    unitsForward = 0


class Plum(Fruit):
    relativeRotation = 90
    unitsForward = 0


# State machine class
class Herbivore(sm.SM):
    # Setting a tuple for start state, this implements the functions
    # While I don't know if the professors do this way for the answer
    startState = 0, 0

    # Initialize the direction of the Herbivore
    direction = 'right'

    def getNextValues(self, state, inp):

        # Move if the Herbivore doesn't turn
        if inp.relativeRotation == 0:
            if self.direction == 'right':
                nextState = self.state[0] + inp.unitsForward, self.state[1]
            elif self.direction == 'left':
                nextState = self.state[0] - inp.unitsForward, self.state[1]
            elif self.direction == 'up':
                nextState = self.state[0], self.state[1] + inp.unitsForward
            elif self.direction == 'down':
                nextState = self.state[0], self.state[1] - inp.unitsForward

        # Turning Counterclockwise
        if inp.relativeRotation == 90:
            if self.direction == 'right':
                nextState = state
                self.direction = 'up'
            elif self.direction == 'left':
                nextState = state
                self.direction = 'down'
            elif self.direction == 'up':
                nextState = state
                self.direction = 'left'
            elif self.direction == 'down':
                nextState = state
                self.direction = 'right'

        # Turning Clockwise
        if inp.relativeRotation == -90:
            if self.direction == 'right':
                nextState = state
                self.direction = 'down'
            elif self.direction == 'left':
                nextState = state
                self.direction = 'up'
            elif self.direction == 'up':
                nextState = state
                self.direction = 'right'
            elif self.direction == 'down':
                nextState = state
                self.direction = 'left'

        # Doing like this, the out put should be the same as the nextState, but maybe can improve
        output = nextState

        return nextState, output


h = Herbivore()
fruits = [Apple(), Apple(), Pear(), Apple(), Pear(), Apple()]
print h.transduce(fruits)

from libdw import sm


class RunOfEvenNumbers(sm.SM):
    startState = 'notDivisible'

    def __init__(self):
        self.counter = 0

    def getNextValues(self, state, inp):
        if state == 'divisible' and inp % 2 == 0:
            self.counter += 1
            nextState = 'divisible'

        elif state == 'divisible' and inp % 2 != 0:
            self.counter = 0
            nextState = 'notDivisible'

        elif state == 'notDivisible' and inp % 2 == 0:
            self.counter = 1
            nextState = 'divisible'

        elif state == 'notDivisible' and inp % 2 != 0:
            self.counter = 0
            nextState = 'notDivisible'

        return nextState, self.counter


m = RunOfEvenNumbers()
m.transduce([1, 2, 3, 7, 4, 2, 7, 2, 8, 2, 8])
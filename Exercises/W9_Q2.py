from libdw import sm


class SimpleAccount(sm.SM):
    def __init__(self, balance):
        self.balance = balance

    startState = 'over'

    def getStartState(self):
        if self.balance >= 100:
            self.startState = 'over'
            return self.startState
        else:
            self.startState = 'below'
            return self.startState

    def getNextValues(self, state, inp):

        nextState = state
        output = self.balance

        if state == 'over' and self.balance + inp >= 100:
            self.balance += inp
            output = self.balance
            nextState = 'over'

        elif state == 'over' and self.balance + inp < 100:
            self.balance += inp
            output = self.balance
            nextState = 'below'

        elif state == 'below' and self.balance + inp < 100:
            if inp >= 0:
                self.balance += inp
                output = self.balance
                nextState = 'below'
            else:
                self.balance += inp
                self.balance -= 5
                output = self.balance
                nextState = 'below'

        elif state == 'below' and self.balance + inp >= 100:
            self.balance += inp
            output = self.balance
            nextState = 'over'

        return nextState, output

acct = SimpleAccount(110)
acct.start()
print acct.step(20)
print acct.step(-30)
print acct.step(-20)
print acct.step(-10)
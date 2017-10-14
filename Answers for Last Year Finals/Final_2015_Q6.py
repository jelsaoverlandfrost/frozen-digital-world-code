from libdw import sm

class Elevator(sm.SM):

    startState = 'First'

    def getNextValues(self, state, inp):
        if state == 'First':
            if inp == 'Up':
                nextState = 'Second'
            elif inp == 'Down':
                nextState = 'First'
        if state == 'Second':
            if inp == 'Up':
                nextState = 'Third'
            elif inp == 'Down':
                nextState = 'First'
        if state == 'Third':
            if inp == 'Up':
                nextState = 'Third'
            elif inp == 'Down':
                nextState = 'Second'

        return nextState, nextState

e = Elevator()
print e.transduce( ['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up'])
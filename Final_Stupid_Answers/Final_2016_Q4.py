from libdw import sm


class RingCounter(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        dictionaryForBinaryValues = {0: '000', 1: '001', 2: '010', 3: '011', 4: '100', 5: '101', 6: '110', 7: '111'}
        if inp == 0:
            if state == 7:
                nextState = 0
                output = dictionaryForBinaryValues[0]
            else:
                nextState = state + 1
                output = dictionaryForBinaryValues[nextState]
        elif inp == 1:
            nextState = 0
            output = dictionaryForBinaryValues[0]
        return nextState, output


print 'test 1'
r = RingCounter()
print r.transduce([0, 0, 0, 0, 0, 0, 0, 0, 0])

print 'test 2'
r = RingCounter()
print r.transduce([0, 0, 0, 1, 0, 0, 0, 0, 0])

print 'test 3'
r = RingCounter()
print r.transduce([0, 0, 0, 1, 0, 0, 1, 0, 0])

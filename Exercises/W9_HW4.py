from libdw import sm


class FirstWordSM(sm.SM):
    startState = 'head'

    def getNextValues(self, state, inp):
        if state == 'head' and inp != ' ' and inp != '\n':
            nextState = 'word'
            output = inp

        elif state == 'head' and inp == ' ':
            nextState = 'head'
            output = None

        elif state == 'head' and inp == '\n':
            nextState = 'head'
            output = None

        elif state == 'word' and inp != ' ':
            nextState = 'word'
            output = inp

        elif state == 'word' and inp == ' ':
            nextState = 'seq'
            output = None

        elif state == 'seq' and inp == '\n':
            nextState = 'head'
            output = None

        elif state == 'seq':
            nextState = 'seq'
            output = None

        return nextState, output


str = 'def f(x): # comment\n   return 1 \n\nhahah\n'
m = FirstWordSM()
m.transduce(str, verbose=True)

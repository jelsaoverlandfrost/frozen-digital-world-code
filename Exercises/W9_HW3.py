from libdw import sm


class CommentsSM(sm.SM):
    startState = 'code'  # fix this

    def getNextValues(self, state, inp):
        if state == 'code' and inp == '#':

            nextState = 'comment'
            output = '#'

        elif state == 'code' and not inp == '#':

            nextState = 'code'
            output = None

        elif state == 'comment' and inp == '\n':

            nextState = 'code'
            output = None

        elif state == 'comment' and not inp == '\n':

            nextState = 'comment'
            output = inp

        return nextState, output


str = 'def f(x): # comment\n   return 1\n #comment \n #coooooo'
m = CommentsSM()
m.transduce(str, verbose=True)
print m.state

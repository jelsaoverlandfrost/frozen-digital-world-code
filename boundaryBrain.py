import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io


class MySMClass(sm.SM):
    startState = 'searching'

    def getNextValues(self, state, inp):
        # print inp.sonars  # list
        # print inp.odometry.theta
        front = round(inp.sonars[2], 2)
        upright = round(inp.sonars[3], 2)
        right = round(inp.sonars[4], 2)

        if state == 'searching':
            if front <= 0.3:
                nextState = 'left'
                output = io.Action(fvel=0, rvel=0)
            elif front > 0.3:
                nextState = 'searching'
                output = io.Action(fvel=0.1, rvel=0)
        elif state == 'left':
            if front >= 0.3 and upright >= round(math.sqrt(2) * right + 0.01, 2):
                nextState = 'forward'
                output = io.Action(fvel=0, rvel=0)
            elif front < 0.3 or upright < round(math.sqrt(2) * right + 0.01, 2):
                nextState = 'left'
                output = io.Action(fvel=0, rvel=0.1)
        elif state == 'forward':
            if front <= 0.3:
                nextState = 'left'
                output = io.Action(fvel=0, rvel=0)
            elif upright >= round(math.sqrt(2) * 0.5 + 0.01, 2):
                nextState = 'right'
                output = io.Action(fvel=0, rvel=0)
            else:
                nextState = 'forward'
                output = io.Action(fvel=0.1, rvel=0)
        elif state == 'right':
            if upright >= round(math.sqrt(2) * 0.5 + 0.01, 2):
                nextState = 'right'
                output = io.Action(fvel=0, rvel=-0.1)
            elif upright < round(math.sqrt(2) * 0.5 + 0.01, 2):
                nextState = 'forward'
                output = io.Action(fvel=0, rvel=0)

        print nextState, front, right, upright, round(math.sqrt(2) * right, 2)
        return nextState, output


mySM = MySMClass()
mySM.name = 'brainSM'


######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar' + str(sonarNum),
                                        lambda:
                                        io.SensorInput().sonars[sonarNum]))


# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False,  # slime trails
                                  sonarMonitor=True)  # sonar monitor widget

    # set robot's behavior
    robot.behavior = mySM


# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks=robot.gfx.tasks())


# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    # print inp.sonars
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())


# called when the stop button is pushed
def brainStop():
    pass


# called when brain or world is reloaded (before setup)
def shutdown():
    pass

import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io


class MySMClass(sm.SM):
    startState = 'away'

    def getNextValues(self, state, inp):
        # print inp.sonars  # list
        # print inp.odometry.theta
        sensor_data = round(inp.sonars[2], 2)
        # speed = abs(0.2 * sensor_data - 0.1)
        if sensor_data > 1:
            output = io.Action(fvel=0.1, rvel=0)
        elif sensor_data >= 0.53:
            output = io.Action(fvel=0.05, rvel=0)
            print '====='
        elif 0.47 < sensor_data < 0.53:
            output = io.Action(fvel=0, rvel=0)
            print "******"
        elif sensor_data <= 0.47:
            output = io.Action(fvel=-0.05, rvel=0)
            print  '-----'
        return state, output


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
    print inp.sonars
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())


# called when the stop button is pushed
def brainStop():
    pass


# called when brain or world is reloaded (before setup)
def shutdown():
    pass

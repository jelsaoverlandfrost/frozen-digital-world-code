from libdw import sm
import time
import serial


class Pump(sm.SM):
    startState = "L"  # lower than 26 C"

    def __init__(self, error4=0, error3=0, error2=0, error1=0, dT=30.5):
        self.desired_temperature = dT
        self.error1 = error1
        self.error2 = error2
        self.error3 = error3
        self.error4 = error4

    # Controller
    def Rotational_Duty_Cycle(self, inp):
        self.error4 = self.error3
        self.error3 = self.error2
        self.error2 = self.error1
        self.error1 = float(inp - self.desired_temperature)

        v = 0.0705222 * self.error1 + 0.5571019 * self.error2 + 0.7654695 * self.error3 + 0.0263793 * self.error4
        p = round(v / 6.0, 3) * 100

        if p > 100.0:
            p = 100.0

        elif p <= 0:
            p = 0.0

        return p

    def getNextValues(self, state, inp):
        TT = self.desired_temperature

        dc = self.Rotational_Duty_Cycle(inp)

        if inp >= TT and state == "L":
            nextState = "H"
            op = dc


        elif inp < TT and state == "L":
            nextState = "L"

            self.error1 = 0
            self.error2 = 0
            self.error3 = 0
            self.error4 = 0

            op = 0.0


        elif inp >= TT and state == "H":
            nextState = "L"
            op = dc

        elif inp < TT and state == "H":
            nextState = "L"
            self.error1 = 0
            self.error2 = 0
            self.error3 = 0
            self.error4 = 0

            op = 0.0

        return nextState, op


pump = Pump()
pump.start()
temperature = 0
ser = serial.Serial(port='/dev/ttyAMA0', baudrate=115200, timeout=None)
while True:
    temperature = float(ser.readline())

    output = pump.step(temperature)
    print 'duty cycle is %f' % output
    ser.write(str(output) + '\n')
# time.sleep(1)
ser.close()

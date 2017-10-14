import os
import glob
import time
import RPi.GPIO as GPIO
from libdw import sm

# Temperature

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f


# Pump

GPIO.setwarnings(False)

m1 = 24  # pin2
m2 = 17  # pin7
m3 = 18  # enable pin


def clockwise():
    GPIO.output(m1, GPIO.HIGH)
    GPIO.output(m2, GPIO.LOW)


def cclockwise():
    GPIO.output(m1, GPIO.LOW)
    GPIO.output(m2, GPIO.HIGH)


def Cease():
    GPIO.output(m1, False)
    GPIO.output(m2, False)


GPIO.setmode(GPIO.BCM)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
GPIO.setup(m3, GPIO.OUT)

p = GPIO.PWM(m3, 10)


# channel=enable pin(18) frequency=10 Hz




class Pump(sm.SM):
    startState = "L"  # lowerthan 26 C" 

    def getNextValues(self, state, inp):
        TT = 26.0
        if state == "L" and inp[0] >= TT:
            nextState = "H"
            op = (1.0, 1.0)
            clockwise()

        elif state == "L" and inp[0] < TT:
            nextState = "L"
            op = (0.0, 0.0)
            Cease()

        elif state == "H" and inp[0] >= TT:
            nextState = "H"
            op = (1.0, 1.0)
            clockwise()

        elif state == "H" and inp[0] < TT:
            nextState = "L"
            op = (0.0, 0.0)
            Cease()

        return nextState, op


Cease()
p.start(100)
c = Pump()
c.start()

while True:
    print (read_temp())
    c.step(read_temp())
    #      counter_clockwise()
    #     for dc in range(0, 101, 5):
    #        p2.ChangeDutyCycle(dc)
    #       time.sleep(5)
    #  for dc in range(100, -1, -5):
    #     p2.ChangeDutyCycle(dc)
    #    time.sleep(5)

p.stop()
GPIO.cleanup()

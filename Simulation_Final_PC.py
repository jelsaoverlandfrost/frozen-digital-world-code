# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:49:05 2017

@author: Thomas
"""
import time
import serial
import simpy
import simpy.rt

ser2 = serial.Serial(port='COM3', baudrate=115200, timeout=None)
print "port opened"

env = simpy.rt.RealtimeEnvironment(factor=0.1, strict=False)
temperature = simpy.Container(env, capacity=100.0, init=100.0)


def change_temp(env):
    while True:
        seconds = env.now
        minutes = seconds / 60
        hour = minutes / 60
        hour = hour % 24
        minutes = minutes % 60
        seconds = seconds % 60

        # print seconds, minutes, hour, days
        if hour <= 24:
            if hour >= 0 and hour < 3:  # temp is 28.0
                room_temp = 28.0

            if hour >= 3 and hour < 4:  # temp is 27.0
                room_temp = 27.0

            if hour >= 4 and hour < 8:  # temp is 27.0
                room_temp = 27.0

            if hour >= 8 and hour < 9:  # temp is 28.0
                room_temp = 28.0

            if hour >= 9 and hour < 10:  # temp is 29.0
                room_temp = 29.0

            if hour >= 10 and hour < 11:  # temp is 30.0
                room_temp = 30.0

            if hour >= 11 and hour < 12:  # temp is 31.0
                room_temp = 31.0

            if hour >= 12 and hour < 13:  # temp is 32.0
                room_temp = 32.0

            if hour >= 13 and hour < 17:  # temp is 32.0
                room_temp = 33.0

            if hour >= 17 and hour < 18:  # temp is 31.0
                room_temp = 31.0

            if hour >= 18 and hour < 19:  # temp is 30.0
                room_temp = 30.0

            if hour >= 19 and hour < 20:  # temp is 29.0
                room_temp = 29.0

            if hour >= 20 and hour < 21:  # temp is 28.0
                room_temp = 28.0

            if hour >= 21:
                room_temp = 28.0

        # convection between algae bottle and surroundings
        Q = 0.29356 * (temperature.level - room_temp)

        # heat loss due to pump
        if temperature.level > 30.5:
            print 'Pump is on'
            ser2.write(str(temperature.level) + '\n')
            power_output = float(ser2.readline().strip())

            Q += power_output * 0.05 * (temperature.level - room_temp)
            # Duty Cycle*1%*5 Watts
        else:
            print 'Pump is off'
        # changes in temperature of algae bottle
        change_in_temp = Q / 167.44

        if Q > 0.0:
            temperature.get(change_in_temp)

        elif Q < 0.0:
            Q = -Q
            temperature.put(change_in_temp)

        print "temperature is %f" % temperature.level
        print hour, minutes, seconds
        yield env.timeout(1)


env.process(change_temp(env))  # tell env to run the process that you have defined
env.run()  # run simulated environment for 20 seconds

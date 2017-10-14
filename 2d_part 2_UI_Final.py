# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 22:20:56 2017

@author: Thomas
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from libdw import sm


class Controller(sm.SM):
    startState = "L"  # lowerthan 26 C" 
    t = 0

    def __init__(self, error4=0, error3=0, error2=0, error1=0):

        self.error1 = error1
        self.error2 = error2
        self.error3 = error3
        self.error4 = error4

        # Controller

    def Rotational_Duty_Cycle(self, inp):
        self.error4 = self.error3
        self.error3 = self.error2
        self.error2 = self.error1
        self.error1 = float(inp[0] - inp[1])

        v = 0.0705222 * self.error1 + 0.5571019 * self.error2 + 0.7654695 * self.error3 + 0.0263793 * self.error4
        p = round(v / 6.0, 3) * 100

        if p > 100.0:
            p = 100.0

        elif p <= 0:
            p = 0.0

        print "error is: %d" % (self.error1)
        print "duty cycle: %d" % (p)

        return p

    def getNextValues(self, state, inp):
        TT = inp[1]
        dc = self.Rotational_Duty_Cycle(inp)

        if inp[0] >= TT and state == "L":
            nextState = "H"
            op = (dc, dc)


        elif inp[0] < TT and state == "L":
            nextState = "L"

            self.error1 = 0
            self.error2 = 0
            self.error3 = 0
            self.error4 = 0

            op = (0.0, 0.0)

        elif inp[0] >= TT and state == "H":
            nextState = "L"
            op = (dc, dc)

        elif inp[0] < TT and state == "H":
            nextState = "L"
            self.error1 = 0
            self.error2 = 0
            self.error3 = 0
            self.error4 = 0

            op = (0.0, 0.0)

        return nextState, op


class ControlSystem(App, sm.SM):
    def TargetTempSliderValue(self, instance, value):
        global c
        self.target_temp.text = str(value) + " Celcius"
        self.output = c.step((self.system_temp_bar.value, self.target_temp_bar.value))
        c.step((self.system_temp_bar.value, self.target_temp_bar.value))

        self.fan_speed.text = "Fan Speed: %.2f" % (self.output[0])
        self.water_pump_speed.text = 'Water Pump Speed: %.2f' % (self.output[1])
        print self.fan_speed.text

    def SystemTempSliderValue(self, instance, value):
        global c
        self.system_temp.text = str(value) + " Celcius"
        self.output = c.step((self.system_temp_bar.value, self.target_temp_bar.value))
        c.step((self.system_temp_bar.value, self.target_temp_bar.value))

        print self.fan_speed.text

        self.fan_speed.text = "Fan Speed: %.2f " % (self.output[0])
        self.water_pump_speed.text = 'Water Pump Speed: %.2f ' % (self.output[1])

    def build(self):
        global c

        self.layout = GridLayout(cols=2)  # specifies 2 columns

        # Blank Placeholders
        blank = Label(text="")
        blank2 = Label(text="")

        # Set Target Temperature



        self.target_temp_bar = Slider(min=0, max=100, value=30.0, step=0.1)
        self.target_temp_bar.bind(value=self.TargetTempSliderValue)

        self.set_target_temp = Label(text="Set Target Temperature")
        self.target_temp = Label(text=str(self.target_temp_bar.value) + " Celcius")

        self.layout.add_widget(self.set_target_temp)
        self.layout.add_widget(self.target_temp)
        self.layout.add_widget(self.target_temp_bar)
        self.layout.add_widget(blank)

        # Set System Temperature



        self.system_temp_bar = Slider(min=0, max=100, value=37.0, step=0.1)
        self.system_temp_bar.bind(value=self.SystemTempSliderValue)

        self.set_system_temp = Label(text="Set System Temperature")
        self.system_temp = Label(text=str(self.system_temp_bar.value) + " Celcius")

        self.layout.add_widget(self.set_system_temp)
        self.layout.add_widget(self.system_temp)
        self.layout.add_widget(self.system_temp_bar)
        self.layout.add_widget(blank2)

        # Fan and Water Pump Speed
        self.output = c.step((self.system_temp_bar.value, self.target_temp_bar.value))

        self.fan_speed = Label(text='Fan Speed: 0')
        self.fan_speed.text = "Fan Speed: %.2f" % (self.output[0])
        print self.fan_speed.text

        self.water_pump_speed = Label(text='Water Pump Speed: 0')
        self.water_pump_speed.text = "Water Pump Speed: %.2f" % (self.output[1])

        self.layout.add_widget(self.fan_speed)
        self.layout.add_widget(self.water_pump_speed)

        # Switch the state machine on and off

        # def update_state(self):     #update state of switch machine
        # if self.state == 'down':
        # self.text = 'On'
        # elif self.state == 'normal':
        # self.text = 'Off'
        # self.system_state = ToggleButton(text = 'Off', on_press = update_state)



        # layout.add_widget(self.system_state)
        return self.layout  # to return gridlayout


c = Controller()
c.start()

if __name__ == '__main__':  # without this, app wont run
    ControlSystem().run()

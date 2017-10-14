#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:33:07 2017

@author: frozen
"""

import math

######### Ignore code below this line ######################################

def f(t, y):
    return 3.0+math.exp(-t)-0.5*y

def approx_ode(h,t0,y0,tn):
######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

######### Add you code below this line
######### Return your answer correct to 3 decimal places

    y = float(y0)
    t = float(t0)
    while t < tn - 0.09:
        y = y + h * f(t, y)
        t = t + h
        print t
    return round(y,3)
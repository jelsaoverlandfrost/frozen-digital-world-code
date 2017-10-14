#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:02:19 2017

@author: frozen
"""

import math
def trapezoidal(a,b):
    answer = (math.e**b + math.e**a) / 2.0 * (b - a)
    return round(answer,2)
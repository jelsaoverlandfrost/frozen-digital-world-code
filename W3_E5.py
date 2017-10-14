#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:42:42 2017

@author: frozen
"""

import math

def f1(x):
    return x**2

def f2(x):
    return math.sin(x)

def f3(x):
    return math.exp(-x)

def simpsons_rule(f, n, a, b):
    sum1 = 0
    sum2 = 0
    h = (b - a) / float(n)
    for j in range(1, n/2):
        sum1 = sum1 + f(a + 2 * j * h)
    for k in range(1, n/2 + 1):
        sum2 = sum2 + f(a + (2 * k - 1) * h)
    result = (h / 3.0) * (f(a) + 2 * sum1 + 4 * sum2 + f(b))
    return round(result,2)
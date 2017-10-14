#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:15:00 2017

@author: frozen
"""
import math

def approx_pi(n):
    sum = 0
    for i in range(n):
        denominator = (math.factorial(i) ** 4) * (396.0 ** (4 * i))
        numerator = math.factorial(4 * i) * (1103.0 + 26390.0 * i)
        sum = sum + numerator / denominator
    result = (2 * math.sqrt(2) / 9801.0) * sum
    result = 1.0 / result
    return result
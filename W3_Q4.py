#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:30:26 2017

@author: frozen
"""

def list_sum(a):
    if len(a) == 0:
        return "0.0"
    sum = 0
    for i in range(0,len(a)):
        sum = sum + a[i];
    return float(sum)
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:29:21 2017

@author: frozen
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        if a < b:
            temp = a
            a = b
            b = temp
        c = b
        d = a % b
        e = gcd(c , d)
        return e
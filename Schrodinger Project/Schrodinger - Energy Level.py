#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:15:09 2017

@author: frozen
"""
import scipy.constants as c

def energy_n(n):
    s1 = c.m_e / (2.0* (c.hbar ** 2.0))
    s2 = (c.e **2.0 / (4.0* c.pi * c.epsilon_0))**2.0
    s3 = 1/(n**2.0)
    joules = float(-1 * (s1 * s2)*s3)
    evolt = float(joules / c.e)
    evolt = round(evolt, 5)
    return evolt
    
print "n=1"
ans = energy_n(1)
print ans
    
print "n=2"
ans = energy_n(2)
print ans
    
print "n=3" 
ans = energy_n(3)
print ans
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:53:35 2017

@author: frozen
"""

def check_value(n1,n2,n3,x):
    if x > n1 and x > n2 and x < n3:
        return True
    else:
        return False
    
print "Test case 1: check_value(1,4,8,7)" 
print "ans = True" 
ans=check_value(1,4,8,7)
print ans
print "Test case 2: check_value(10,4,8,7)" 
print "ans = False" 
ans=check_value(10,4,8,7)
print ans
print "Test case 3: check_value(1,10,8,7)" 
print "ans = False" 
ans=check_value(1,10,8,7)
print ans
print "Test case 4: check_value(1,4,5,7)" 
print "ans = False" 
ans=check_value(1,4,5,7)
print ans

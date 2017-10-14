#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:02:53 2017

@author: frozen
"""

def temp_convert(type, temp):
    if type == "F":
        return celsius_to_farenheit(temp)
    elif type == "C":
        return farenheit_to_celsius(temp)
    else:
        return None
    
######### Ignore code below this line ######################################
def farenheit_to_celsius(F):
    C = (F-32)*float(5)/9
    return C

def celsius_to_farenheit(C):
    F = C*float(9)/5 + 32
    return F
    
print "Test case 1: C = 32" 
ans=temp_convert("F", 32) 
print ans
print "Test case 2: C = -40" 
ans=temp_convert("F", -40) 
print ans
print "Test case 3: C= 212" 
ans=temp_convert("F", 212) 
print ans
print "Test case 4: F = 0" 
ans=temp_convert("C", 0) 
print ans
print "Test case 5: F = -40" 
ans=temp_convert("C", -40) 
print ans
print "Test case 6: F = 100" 
ans=temp_convert("C", 100) 
print ans
print "Test case 7: Neither 'C' nor 'F'"
ans=temp_convert("", 0)
print ans
print "Test case 8: Neither 'C' nor 'F'"
ans=temp_convert("A", 0)
print ans
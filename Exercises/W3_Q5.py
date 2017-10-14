#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:34:38 2017

@author: frozen
"""

import sys

def minmax_in_list(ls):
    #In Case
    if len(ls) == 0:
        return (None , None)
    #Initialize
    max = ls[0];
    min = ls[0];
    for i in range(0,len(ls)):
        if ls[i] > max:
            max = ls[i]
        if ls[i] < min:
            min = ls[i]
    return (min , max)

print ("Test case 1: [1,2,3,4,5]") 
ans=minmax_in_list([1,2,3,4,5]) 
print ans
print ("Test case 2: [1,1,3,0]") 
ans=minmax_in_list([1,1,3,0]) 
print ans
print ("Test case 3: [3,2,1]") 
ans=minmax_in_list([3,2,1]) 
print ans
print ("Test case 4: [0,10]") 
ans=minmax_in_list([0,10]) 
print ans
print ("Test case 5: [1]") 
ans=minmax_in_list([1]) 
print ans
print ("Test case 6: []") 
ans=minmax_in_list([]) 
print ans
print ("Test case 7: [1,1,1,1,1]") 
ans=minmax_in_list([1,1,1,1,1]) 
print ans
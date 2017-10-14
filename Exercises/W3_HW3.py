#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:14:05 2017

@author: frozen
"""

def get_even_list(ls):
    result = []
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            result.append(ls[i])
    return result

print "get_even_list([1,2,3,4,5])" 
ans=get_even_list([1,2,3,4,5]) 
print ans
print "get_even_list([11,22,33,44,55])" 
ans=get_even_list([11,22,33,44,55]) 
print ans
print "get_even_list([10,20,30,40,50])" 
ans=get_even_list([10,20,30,40,50]) 
print ans
print "get_even_list([11,21,31,41,51])" 
ans=get_even_list([11,21,31,41,51]) 
print ans
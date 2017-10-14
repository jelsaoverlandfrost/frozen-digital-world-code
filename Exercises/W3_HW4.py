#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:23:33 2017

@author: frozen
"""

def is_prime(n):
    check = True
    
    #In case:
    if n == 0 or n == 1:
        check = False
    
    for i in range(2,n):
        if n % i == 0:
            check = False
            break
    return check

print "is_prime(2)" 
ans=is_prime(2) 
print ans
print "is_prime(3)" 
ans=is_prime(3) 
print ans
print "is_prime(7)" 
ans=is_prime(7) 
print ans
print "is_prime(9)" 
ans=is_prime(9) 
print ans
print "is_prime(21)" 
ans=is_prime(21) 
print ans
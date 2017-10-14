#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:43:43 2017

@author: frozen
"""

def is_palindrome(num):
    string = str(num)
    length = len(string)
    check = True
    for i in range(0,length/2):
        if string[i] != string[length - i - 1] :
            check = False
            break
    return check

print ("Test case 1: 1") 
ans=is_palindrome(1) 
print ans
print ("Test case 2: 22") 
ans=is_palindrome(22) 
print ans
print ("Test case 3: 12321") 
ans=is_palindrome(12321) 
print ans
print ("Test case 4: 441232144") 
ans=is_palindrome(441232144) 
print ans
print ("Test case 5: 441231144") 
ans=is_palindrome(441231144) 
print ans
print ("Test case 6: 144") 
ans=is_palindrome(144) 
print ans
print ("Test case 7: 12") 
ans=is_palindrome(12) 
print ans
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:02:40 2017

@author: frozen
"""

def printvals(n):
    ans = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 7 ==0:
            ans.append('AB')
        elif i % 5 == 0:
            ans.append('A')
        elif i % 7 == 0:
            ans.append('B')
        else:
            ans.append(i)
    return ans
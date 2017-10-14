#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:57:41 2017

@author: frozen
"""

def transpose_matrix(a):
    b = []
    for j in range(len(a[0])):
        b.append([0]*len(a))
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[j][i] = a[i][j]
    return b
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:08:37 2017

@author: frozen
"""

def my_reverse(list1):
    print list1
    length = len(list1)
    list2 = [None] * length
    for i in range(length):
        list2[i] = list1[length - i - 1]
        print list1
    return list2
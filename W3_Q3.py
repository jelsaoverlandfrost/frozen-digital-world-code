#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:18:13 2017

@author: frozen
"""
def letter_grade(mark):
    if mark >= 90 and mark <= 100:
        return "A"
    elif mark >= 80 and mark < 90:
        return "B"
    elif mark >= 70 and mark < 80:
        return "C"
    elif mark >= 60 and mark < 70:
        return "D"
    elif mark < 60 and mark >= 0:
        return "F"
    else:
        return "None"
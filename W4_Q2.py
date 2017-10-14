#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:05:22 2017

@author: frozen
"""

def compound_value_months(monthlyAmt, annualRate, months):
    sums = 0
    monthlyRate = annualRate / 12.0
    for i in range(months):
        sums = (sums + monthlyAmt) * (1 + monthlyRate)
    return round(sums,2)
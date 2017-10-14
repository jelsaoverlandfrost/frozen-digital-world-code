#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:01:32 2017

@author: frozen
"""
import types

def may_ignore(x):
    if type(x) == types.IntType:
        x = x + 1
        return x
    else:
        return None
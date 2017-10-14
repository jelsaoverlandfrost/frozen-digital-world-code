#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:27:54 2017

@author: frozen
"""

####### Your function should return a tuple containing a list of average #####
####### and the overall average, e.g., ([3.5,6.0,1.4], 3.625) ################  

def find_average(listOfLists):
    listOfAvg = []
    avg = 0
    totalSum = 0
    lengthSum = 0
    for i in range(len(listOfLists)):
        subSum = 0
        subAvg = 0
        lengthSum = lengthSum + len(listOfLists[i])
        for j in range(len(listOfLists[i])):
            subSum = subSum + listOfLists[i][j]
            totalSum = totalSum + listOfLists[i][j]
        if len(listOfLists[i]) == 0:
            subAvg = 0
        else:
            subAvg = subSum / float(len(listOfLists[i]))
        listOfAvg.append(subAvg)
        avg = totalSum / float(lengthSum)
    return (listOfAvg,avg)
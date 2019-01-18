#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 13:04:32 2019

@author: xupech
"""

def how_many (aDict):
    values = 0
    for i in aDict:
        values += len(aDict [i])
    return values
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 13:09:27 2019

@author: xupech
"""

def biggest(aDict):
    compare_value = []
    for keys in aDict.values():
        compare_value += [len(aDict.values())]
        big_value = max(compare_value)
    return big_value
    print (big_value)
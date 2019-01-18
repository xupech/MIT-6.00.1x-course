#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:30:06 2019

@author: xupech
"""

"""paying debt problem"""

b0 = float(input('balance:'))
i= float(input('annual interest rate:'))
p = float(input('minimum monthly payment rate:'))
m = 12

def pay(b0, i, p, m):

    if m == 0:
        return b0
    else:
        v = pay(b0, i, p, m-1)
        return v-v*p+(v-v*p)*i/12

print (pay(b0, i, p, m))
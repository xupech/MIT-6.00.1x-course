#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:28:31 2019

@author: xupech
"""
b0 = float(input('balance:'))
i= float(input('annual interest rate:'))
p = float(input('minimum monthly payment rate:'))
m = 12

while m > 0:
    b0 = b0 - b0* p
    b0 = b0 + b0* i/12
    m-=1
b0 = round (b0,2)

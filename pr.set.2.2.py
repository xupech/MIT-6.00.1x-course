#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 20:26:38 2019

@author: xupech
"""

""" minimum payment problem"""
b0 = float(input('balance:'))
i= float(input('annual interest rate:'))
min_pay = 0
m = 12  

def pay(b0, min_pay, m):
    while m > 0:
        b0 = b0-min_pay+(b0-min_pay)*i/12
        m-=1
    return b0

while pay(b0, min_pay, m) > 0:
    min_pay+=10
    pay(b0, min_pay, m)
    
print (min_pay)
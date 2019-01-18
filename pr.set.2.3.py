#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 21:00:30 2019

@author: xupech
"""

""" minimum payment problem, bisection research"""

b0 = float(input('balance:'))
i= float(input('annual interest rate:'))

l_bound = b0/12
u_bound = (b0*(1+i/12)**12)/12
epsilon = 0.01

min_pay = (l_bound+u_bound)/2

def pay(b0, min_pay):
    m = 1
    while m <=12:
        b0 = b0-min_pay+(b0-min_pay)*i/12
        m+=1 
        
    round (b0,2)
    return b0

while abs(pay(b0, min_pay)) > epsilon:
    if pay(b0, min_pay) > 0:
        l_bound = min_pay
        min_pay = (l_bound+u_bound)/2
        pay(b0, min_pay)
        
    elif pay(b0, min_pay) < 0:
        u_bound = min_pay
        min_pay = (l_bound+u_bound)/2
        pay(b0, min_pay)
    round (min_pay, 2)
print (min_pay)
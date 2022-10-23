# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:18:12 2022

@author: Sandy
"""

import matplotlib.pyplot as plt 
import math
import random
from statistics import mean
import time

# initiating the number of iterations to be n=100000
t_0=0
tf=100
t=0.001
r_0=0
r_1=0
r_2=0
n=int((tf-t_0)/t)
# initiating the number of spaces on the graph to be n+2(To have a better and clear graph)
x=[None]*(n+2)
y=[None]*(n+2)
z=[None]*(n+2)
# writing the function for x,y and z initiating a for loop to get our n iterations and using a random function so that it assumes a random number every iteration
for i in range(0,n+1):
    rx=float(r_0+math.sqrt(6/t)*t*random.uniform(-1,1))
    ry=float(r_1+math.sqrt(6/t)*t*random.uniform(-1,1))
    rz=float(r_2+math.sqrt(6/t)*t*random.uniform(-1,1))
    x[i]=rx
    y[i]=ry
    z[i]=rz
    print(f"rx value is {rx},ry value is {ry} and rz value is {rz}")
    r_0=rx
    r_1=ry
    r_2=rz
    #plotting our graph of x vs y
# plt.plot(x,y)
# #labelling the axis
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()
# MSD=[None]*(10000)
u=0
lst = []
for j in  range(1,11):
    for i in  range(0,11-j):
        print(j,i)
        k= u + (((x[i+j]-x[i])**2)+((y[i+j]-y[i])**2)+((z[i+j]-z[i])**2))
        # print(f"k is {k}")
        u=k
        MSD=k/(10001-j)
        lst.append(MSD)
    print(f"Mean Square Displacement is {MSD}")
    
    

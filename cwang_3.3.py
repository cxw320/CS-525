'''
Caroline Wang
CS 525
3/30/2018
Homework Problem 3.3
Description: Write a program that finds the GPS locations for a series of cities and computes the estimated area enclosed by the four cities
'''

import math

#cities = {'atlanta':[31, 31]}

atlanta = [39.55, -116.25]

orlando = [41.5, 87.37]

cities = [[ [39.55, -116.25], [41.5, 87.37] ], [ [41.5, 87.37], [30.55, -100] ] ]



for e in cities:
    print(e[0][0])
    print(e[0][1])
    print(e[1][0])
    print(e[0][1])

'''for e in cities:

    x1 = math.radians(e[0][0])   # latitude of 1st location
    x2 = math.radians(e[0][1])   #longitude of 1st location

    y1 = math.radians(orlando[1][0])   # latitude of 2nd location
    y2 = math.radians(orlando[1][1])  # longitude of 2nd location

    radius = 6371.01


    d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

    print(d)
    
    '''

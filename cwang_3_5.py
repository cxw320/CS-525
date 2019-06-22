'''
Caroline Wang
CS 525
3/30/2018
Homework Problem 3.5
Description: Write a program that displays the area for a polygon after a user enters the number of sides and their length
'''

import math

sides_input = int(input("Enter the number of sides:"))

length_input = float(input("Enter the side:"))

area = ( sides_input * length_input**2)  / (4 * math.tan(math.pi/sides_input))

print(area)
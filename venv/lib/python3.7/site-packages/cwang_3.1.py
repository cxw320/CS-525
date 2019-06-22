'''
Caroline Wang
CS 525
3/30/2018
Homework Problem 3.5
Description: Write a program that calculates the area of a pentagon using the length from the center of a pentagon to a vertex
'''

import math   #Imports the math module since we require pi, sin and square root functions

r_input = float(input("Enter the length from the center to a vertex: "))  #Converts a user input for r into a float


s = 2 * r_input * math.sin(math.pi/5) #Calculates a side using the input (r) and the sin and pi function from the math module


area = round(3 * math.sqrt(3) / 2 * s**2 ,2) #Calculates an area using the square root function in the math module


template = "The area of the pentagon is {0}" #Use print.format to print the final statement for pentagon area

print(template.format(area))




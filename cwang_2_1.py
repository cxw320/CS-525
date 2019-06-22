'''
Caroline Wang
CS 525
3/30/2018
Homework Problem 2.1
Description: Write a program that reads Celsius degree from the console and displays converted Fahrenheit
'''

#Below is the user input for Celsius degree assigned to variable 'celsius_input'

celsius_input = input("Enter a degree in Celsius:")

#Below formula assigns also the celsius_input as a float when using it in the fahrenheit conversion formula

fahrenheit = ( 9 / 5) * float(celsius_input) + 32

#Below is the final print statement to display the fahrenheit value

template = "{0} Celsius is {1} Fahrenheit"

print(template.format(celsius_input,fahrenheit))

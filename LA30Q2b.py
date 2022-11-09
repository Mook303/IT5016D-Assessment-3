Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LA30Q2b.py
#
# author: M. J. Stephenson
# date: October 2022
import math
side_x = int(input("Please enter the radius of the circle\n\n"))
print("\nThe area of your shape is ", side_x ** 2 * math.pi * 3/4 ,"\n\n")
# Testing
'''
print("My assertions are:"
      "\nx = 5, output = 58.9"
      "\nx = 7, output = 115.5")
'''
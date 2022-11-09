Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LA30Q2c.py
#
# author: M. J. Stephenson
# date: October 2022
import math
side_g = int(input("Please enter the length of side f\n\n"))
side_e = int(input("Please enter the length of side g\n\n"))
side_f = int(input("Please enter the length of e\n\n"))
print("\nThe area of your shape is ",
      side_f / 2 * side_g
      + side_e * side_g
      + (side_g/2) ** 2 * math.pi/2
      ,"\n\n")
# Testing
'''
print("My assertions are:"
      "\ng = 6, e = 6, f = 6, output = 68.14"
      "\ng = 7, e = 2, f = 9, output = 64.74")
'''
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LA30Q3b.py
#
# author: M. J. Stephenson
# date: October 2022
import math
side_f = int(input("Please enter the length of side f\n\n"))
print("\nThe area of your shape is ",
      # half the base, times the height
      side_f / 2 * side_f * math.cos(math.radians(40))
      ,"\n\n")
# Testing
'''
print("My assertions are:"
      "\nf = 5, output = 9.6"
      "\ne = 7, output = 18.8")
'''
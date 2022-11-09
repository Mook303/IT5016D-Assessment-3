Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LA30Q3a.py
#
# author: M. J. Stephenson
# date: October 2022
import math
side_e = int(input("Please enter the length of side e\n\n"))
side_d = int(input("Please enter the length of side d\n\n"))
print("\nThe area of your shape is ",
      # half the base, times the height
      side_d / 2 * math.sqrt(side_e ** 2 - side_d ** 2)
      ,"\n\n")
# Testing
'''
print("My assertions are:"
      "\ne = 5, d = 4,  output = 6"
      "\ne = 25, e = 24,  output = 84")
'''
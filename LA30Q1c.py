Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LA30Q1c.py
#
# author: M. J. Stephenson
# date: October 2022
side_u = int(input("Please enter the length of the rectangle\n\n"))
side_m = int(input("Please enter the width of the rectangle\n\n"))
side_n = int(input("Please enter the length of the side of the triangle\n\n"))
print("\nThe area of your shape is ",
      side_u * side_m
      + side_n / 2 * side_n
      ,"\n\n")
# Testing
'''
print("My assertions are:"
      "\nu = 5, m = 3, n = 5 output = 27.5"
      "\nu = 2, m = 1, n = 5 output = 14.5")
'''
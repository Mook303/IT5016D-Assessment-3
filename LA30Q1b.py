Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LA30Q1b.py
#
# author: M. J. Stephenson
# date: October 2022
side_q = int(input("Please enter the length of the small rectangle\n\n"))
side_w = int(input("Please enter the width of the small rectangle\n\n"))
side_s = int(input("Please enter the length of the large rectangle\n\n"))
side_g = int(input("Please enter the width of the large rectangle\n\n"))
print("\nThe area of your shape is ", side_g * side_s - side_q * side_w,"\n\n")
# Testing
'''
print("My assertions are:"
      "\nq = 5, w = 3, s = 8, g = 4 output = 17"
      "\nq = 2, w = 1, s = 5, g = 3 output = 13")
'''
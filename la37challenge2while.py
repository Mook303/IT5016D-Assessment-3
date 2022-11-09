# LA37 Challenge2While.py
#
# @ author: M. J. Stephenson
# date: October 2022

number = int(input("Please enter a number\n\n"))
counter = 0
total = 0 

while counter <= number:
        total = total + counter
        counter += 1 
        
print("\nn = ", number, " sum = ",total,"\n\n")
# LA37 Challenge3While.py
#
# @ author: M. J. Stephenson
# date: October 2022

p = int(input("Please enter an increment\n\n"))
q = int(input("Please enter an ending number\n\n"))

counter = 10
number = 10

starting_number = (10 % p) + 10

while counter < q:
        print(starting_number,end=", ")
        starting_number = starting_number + p
        counter += p
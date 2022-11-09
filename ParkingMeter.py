# ParkingMeter2.py
#
# @ author: M. J. Stephenson
# date: November 2022
 
print ("Kia Ora, this is a parking meter")
park_time = 4
print ("park_time time is ", park_time, " hours.")
 
rate = 4
cost = 0
if park_time > 3:
    cost = rate *3
    # drop the rate by $2
    rate -= 2
    # get the remainder of the parking time
    park_time -= 3
    # add to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print ("The cost of the parking is $", cost)
    
print ("How many hours would you like to park?")

if park_time > 3:
    cost = rate *3
    # drop the rate by $2
    rate -= 2
    # get the remainder of the parking time
    park_time -= 3
    # add to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print ("The cost of the parking is $", cost)
 

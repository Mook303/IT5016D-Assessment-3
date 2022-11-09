# Quiz.py
#
# author: A. N. Other
# date: September 2016
from datetime import datetime
score = 0
start_time = datetime.today()
answer_one = (input("Where is Te Papa Mueseum?\n\n"))
if answer_one.lower() == "wellington":
    score = score + 1
    print("\nThat is correct. Your current score is ", score ,"\n\n")
else:          
    print("\nThat is incorrect. Your current score is still", score ,"\n\n")
answer_two = (input("Who is the indigenous people of New Zealand?\n\n"))    
if answer_two.lower() == "maori":
    score = score + 1
    print("\nThat is correct. Your current score is ", score ,"\n\n")
else:          
    print("\nThat is incorrect. Your current score is still", score ,"\n\n")
answer_three = (input("who is the prime-minister of New Zealand?\n\n"))    
          
if answer_three.lower() == "jacinda ardern":
    score = score + 1
    print("\nThat is correct. Your current score is ", score ,"\n\n")
else:          
    print("\nThat is incorrect. Your current score is still", score ,"\n\n")
answer_four = (input("Queenstown is in which Island of New Zealand?\n\n"))    
          
if answer_four.lower() == "south island":
    score = score + 1
    print("\nThat is correct. Your current score is ", score ,"\n\n")
else:          
    print("\nThat is incorrect. Your current score is still", score ,"\n\n")
answer_five = (input("Which city is the sky tower in?\n\n"))    
          
if answer_five.lower() == "auckland":
    score = score + 1
    print("\nThat is correct. Your current score is ", score ,"\n\n")
else:          
    print("\nThat is incorrect. Your current score is still", score ,"\n\n")
print("\nYour final score is ", score ,"\n\n")
print("The time taken for you to complete this quiz is....", datetime.today() - start_time)



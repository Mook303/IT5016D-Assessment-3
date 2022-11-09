# LA37 Challenge4While.py
#
# @ author: M. J. Stephenson
# date: October 2022

password = (input("Please enter a password\n\n"))
stored_password_variable = "Welcome1234"
counter = 0 
correct_flag = False

while counter < 2 and correct_flag == False:
        if password == stored_password_variable:
            print("\nCorrect password\n\n")
            correct_flag = True
        elif password == "Exit":
            print("\nProgramme terminated\n\n")
            correct_flag = True
        else:
              print("\nIncorrect password\n\n")
              password = (input("Please enter a password\n\n"))
              counter += 1
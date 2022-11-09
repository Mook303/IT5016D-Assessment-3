# LA37 Challenge5While.py
#
# @ author: M. J. Stephenson
# date: October 2022

guess = int(input("Guess a number\n\n"))
last_guess = int
secret_number = 42
counter = 0    
found = False

while found != True:
         if guess > secret_number:
                 print("\nToo high try again\n\n")
                 if last_guess != guess:
                     counter +=1 
                 last_guess = guess 
                 guess = int(input("Guess a number\n\n"))
         elif guess < secret_number:
                 print("\nToo low try again\n\n")
                 if last_guess != guess:
                       counter +=1 
                 last_guess = guess
                 guess = int(input("Guess a number\n\n"))
         else:
                 counter +=1 
                 print("\nThat is correct!\n\n")
                 found = true

print("\nYou had ", counter, " guesses\n\n")
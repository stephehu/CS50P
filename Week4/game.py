# I’m thinking of a number between 1 and 100…

# What is it?
# In a file called game.py, implement a program that:

# Prompts the user for a level, 
# . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and 
# , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, 
# the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

import random


while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break # n is valid, exit the loop
    except ValueError:
        pass
    
i = random.randint(1, n)

while True:
    try: 
        guess = int(input("Guess: "))
        if guess < 1:
            continue # guess is invalid, skip input and reprompt
        if guess < i:
            print("Too small!")
        elif guess > i:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
        

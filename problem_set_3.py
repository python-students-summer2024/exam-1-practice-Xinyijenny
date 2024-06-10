"""
Your job is to complete the definitions of each function mentioned in the comments so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

import random

##--------------------- Function #1 ---------------------##
# Define a function named 'get_random_int'.  
# This function accepts two arguments: a minimum value and a maximum value.
# The function must return a random integer between these two values, inclusive.
# Use the function random.randint() to generate the pseudo-random number.
def get_random_int(min,max):
    return random.randint(min,max)
  



##--------------------- Function #2 ---------------------##
# Define a function named 'get_guess'.
# This function accepts a single argument - an integer that serves as a max value.
# This function asks the user once to guess a random integer between 1 and the max value, inclusive.
# The function calls the function named get_random_int in order to generate the random integer in this range.
# If the user has entered an invalid response (i.e. anything that is not an integer in this range), the function returns an integer, -1.
# If the user has guessed the random integer correctly, this function returns a boolean True.
# If the user has guessed incorrectly, this function returns a boolean False.
def get_guess(max):
    unumber = input(f"Guess the integer between 1 and {max}:")
    if not unumber.isnumeric():
        return -1
    
    unumber = int(unumber)
    if unumber >= 1 and unumber <= max:# find out if user number in range
        rnumber = get_random_int(1,max) # generating a number 
        if unumber == rnumber:
            return True
        else:
            return False
    else:
        return -1





##--------------------- Function #3 ---------------------##
# Define a function named 'play_game'.
# This function does not accept any arguments.
# This function uses the get_guess function to ask the user four times to guess a random integer between 1 and 5, inclusive.
# Each time the user guesses, they are immediately informed whether they guessed correctly or not, with the printed output, "Correct!" or "Wrong!"
# If at any time, the user enters an invalid response, the program immediately prints out the text, "Invalid response!" and does not print out anything further.
# At the end, the function, assuming the user has entered all valid guesses, the program prints out the percent of guesses that user guessed correctly, following the format: "You guessed 75% of the random numbers correctly."

def play_game():
    persent = 0
    game = get_guess(5) #round1
    if game == -1:
        print("Invalid response!")

    else:#if it is valid
        if game is True:
            print("Correct!")
            persent = persent + 1
            
        elif game is False:
            print("Wrong!")
        
        game = get_guess(5) #round2
        if game == -1:
            print("Invalid response!")

        else:#if it is valid
            if game is True:
                print("Correct!")
                persent = persent + 1
            elif game is False:
                print("Wrong!")
            
            game = get_guess(5) #round3
            if game == -1:
                print("Invalid response!")

            else:#if it is valid
                if game is True:
                    print("Correct!")
                    persent = persent + 1
                elif game is False:
                    print("Wrong!")

                game = get_guess(5) #round4
                if game == -1:
                    print("Invalid response!")

                else:#if it is valid
                    if game is True:
                        print("Correct!")
                        persent = persent + 1
                    elif game is False:
                        print("Wrong!")
                    print(f"You guessed {persent * 25}% of the random numbers correctly.")
                            
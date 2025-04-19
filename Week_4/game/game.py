#CS50 assignment:  implement a program that:

# Prompts the user for a level, 

# If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, 
#       the program should prompt the user again.

#       If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#       If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#       If the guess is the same as that integer, the program should output Just right! and exit.

import random

def main():
    get_guess()
    
def get_input():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print("You must input a positive integer for level")
        else:
            if level > 0:
                break
            else:
                print("The level must be a positive integer")
    return(level)

def get_guess():
    level = get_input()
    number = random.randint(1, level+1)

    while True:
        try:
            guess = int(input(f"Guess the number, between 1 and {level}: "))
        except ValueError:
            print("Your guess must be a positive integer")
        else:
            if guess > 0:
                if guess < number:
                    print("Too small!")
                elif guess > number:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
            else:
                print("Your guess must be a positive integer")



if __name__ == "__main__":
    main()
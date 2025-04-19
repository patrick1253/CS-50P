# CS50 assignment:  implement a program that:

#   Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
#   Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a 
#       non-negative integer with n digits. No need to support operations other than addition (+).
#    Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), 
#       the program should output EEE and prompt the user again, allowing the user up to three tries in total 
#       for that problem. If the user has still not answered correctly after three tries, the program should 
#       output the correct answer.
#   The program should ultimately output the user’s score: the number of correct answers out of 10.

# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a 
# level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with 
# level digits or raises a ValueError if level is not 1, 2, or 3:


import random
import inflect
p = inflect.engine()

def main():
    level = get_level()
    
    correct = 0
    attempted = 0

    for i in range(1, 11):
        numbers = generate_integer(level)
        x = numbers[0]
        y = numbers[1]
        correct_answer = x + y
        attempted += 1
        tries = 3

        while True:
            user_answer = int(input(f"{str(x)} + {str(y)} = ")) 
            if user_answer == correct_answer:
                print("Correct!")
                correct += 1
                break
            else:
                tries -= 1
                if tries > 0:
                    print(f"EEE.  You have {tries} " + p.singular_noun("attempts", tries) + " left")
                elif tries == 0:
                    print(f"EEE.  You have run out of attempts. The correct answer is {x} + {y} = {correct_answer}")
                    break
    
    print(f"Your score is {correct} correct " + p.singular_noun("answers ", correct) + f"out of {attempted} " + 
          p.singular_noun("problems", attempted) + " attempted")
       

def get_level():
    while True:
        level = int(input("Level, between 1 and 3: "))
        if 1 <= level <=3:
            break
    return level


def generate_integer(level):
    numbers = []
    
    x = random.randint(1,(10**level))
    numbers.append(x)
    
    y = random.randint(1,(10**level))
    numbers.append(y)

    return numbers

if __name__ == "__main__":
    main()

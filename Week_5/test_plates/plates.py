# CS50 assignment: In Massachusetts, home to Harvard University, it’s possible to request 
# a vanity license plate for your car, with your choice of letters and numbers instead of 
# random ones. Among the requirements, though, are:

#    “All vanity plates must start with at least two letters.”
#    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a 
#       minimum of 2 characters.”
#    “Numbers cannot be used in the middle of a plate; they must come at the end. For 
#       example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
#       The first number used cannot be a ‘0’.”
#    “No periods, spaces, or punctuation marks are allowed.”

# In plates.py, implement a program that prompts the user for a vanity plate and then output 
# Valid if meets all of the requirements or Invalid if it does not. Assume that any letters 
# in the user’s input will be uppercase. Structure your program per the below, wherein is_valid 
# returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
# You’re welcome to implement additional functions for is_valid to call (e.g., one function 
# per requirement).

import string

def main():
    plate = input("Type your requested vanity plate: ")
    print(is_valid(plate))


def is_valid(text):

    # test length is at least 2 and no more than 6 characters long
    if 2 > len(text) or len(text) > 6:
        print("Invalid: Length must be 2-6 characters")
        return ("Invalid")

    # test that first two characters are letters
    if not (text[0].isalpha()) or not(text[1].isalpha()):
        print("Invalid: First two characters must be letters")
        return ("Invalid")

    # Number of columns (counting from the left) that have letters or numbers
    letters_count = 0
    numbers_count = 0

    for char in text: 

        # check for punctuation marks
        if char in string.punctuation:
            print("Invalid: Cannot include punctuation marks")
            return ("Invalid")

        if char.isalpha():
            letters_count += 1
            #print(f"letters to the left = {letters_count}")
        
        if char.isnumeric():
            numbers_count += 1
            #print(f"numbers to the left = {numbers_count}")
        
        # check that no letters follow numbers (i.e.: that numbers are not in the middle)
        if char.isalpha() and numbers_count >= 1:
            print("Invalid: No letters can follow numbers")
            return ("Invalid")
        
        # check that first number to appear (reading left to right) is not a zero
        if char == str("0") and numbers_count == 1:
            print("Invalid: First number cannot be 0")
            return ("Invalid")
        
    return ("Valid")

if __name__ == "__main__":
    main()
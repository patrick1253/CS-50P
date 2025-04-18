# CS50 assignment: In a file called emojize.py, implement a program 
# that prompts the user for a str in English and then outputs the 
# “emojized” version of that str, converting any codes (or aliases) 
# therein to their corresponding emoji.

from emoji import emojize

def main():
    print_emoji()

def print_emoji():
    emoji = (input("What emoji would you like? "))
    print (emojize(emoji, language='alias'))

if __name__ == "__main__":
    main()    

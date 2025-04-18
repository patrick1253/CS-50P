# CS50 assignment:  In a file called figlet.py, implement a program that:

#    Expects zero or two command-line arguments:
#        Zero if the user would like to output text in a random font.
#        Two if the user would like to output text in a specific font, 
#             in which case the first of the two should be -f or --font, 
#             and the second of the two should be the name of the font.
#    Prompts the user for a str of text.
#    Outputs that text in the desired font.

# If the user provides two command-line arguments and the first is 
# not -f or --font or the second is not the name of a font, the program 
# should exit via sys.exit with an error message.

import random
import sys
import pyfiglet
from pyfiglet import Figlet

def main():
    make_figlet()

# From the command line interface, the program should be called using "-f" or "--font"
# followed by the name of the desired font (eg: "python figlet.py -f slant").  
# Leaving one of these blank will result in an error.  Leaving both of these blank 
# will result in a random choice of font.

def make_figlet():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(fonts))
    
    elif len(sys.argv) == 2 or sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Input -f or --font, followed by the name of the desired font")
    
    elif len(sys.argv) == 3 and sys.argv[2] in fonts:
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit("Input -f or --font, followed by the name of the desired font")


    text = input("Desired text: ")                 
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
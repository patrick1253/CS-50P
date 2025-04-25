# CS50 assignment: implement a program that expects exactly one command-line argument, the name 
# (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using 
# tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s 
# grid format. If the user does not specify exactly one command-line argument, or if the specified 
# file’s name does not end in .csv, or if the specified file does not exist, the program should 
# instead exit via sys.exit.

from tabulate import tabulate
import sys

def main():
    menu = sys.argv[1:]
    print(make_table(menu))

def make_table(menu):

    if len(menu) > 1:
        sys.exit("Too many CLI arguments")
    else:
        menu = menu[0]

    suffix = menu.split('.')[-1]

    if suffix != "csv":
        sys.exit("Not a CSV file")

    try:
        file = open(menu, "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return tabulate(menu, grid)
    
if __name__ == "__main__":
    main()

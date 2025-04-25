# CS50 assignment: implement a program that expects exactly one command-line argument, the name 
# (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using 
# tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s 
# grid format. If the user does not specify exactly one command-line argument, or if the specified 
# file’s name does not end in .csv, or if the specified file does not exist, the program should 
# instead exit via sys.exit.

from tabulate import tabulate
import sys
import csv

def main():
    filename = sys.argv[1:]
    print(make_table(filename))

def make_table(filename):

    menu = []

    if len(filename) > 1:
        sys.exit("Too many CLI arguments")
    elif len(filename) < 1:
        sys.exit("Too few CLI arguments")
    else:
        filename = filename[0]

    suffix = filename.split('.')[-1]

    if suffix != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return tabulate(menu, headers="firstrow", tablefmt="grid")
    
if __name__ == "__main__":
    main()

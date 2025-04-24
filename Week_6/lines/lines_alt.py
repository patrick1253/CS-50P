# CS50 assignment: in a file called lines.py, implement a program that expects exactly one 
# command-line argument, the name (or path) of a Python file, and outputs the number of lines 
# of code in that file, excluding comments and blank lines. If the user does not specify exactly 
# one command-line argument, or if the specified file’s name does not end in .py, or if the 
# specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring 
# should not be considered a comment.) Assume that any line that only contains whitespace is blank.

import sys

def main():
    filename = sys.argv[1:]
    line_count = valid_file(filename)
    print(f"Number of lines in {filename[0]}: {line_count}")

def valid_file(filename):

    if (len(filename)) > 1:
        sys.exit("Too many command-line arguments")
    else:
        filename = filename[0]    

    suffix = (filename.split('.')[-1])
          
    if suffix != "py":
        sys.exit("Not a python filename")

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return count_lines(file)


def count_lines(file):
    line_count = 0
    
    for line in file:
        if line.lstrip().startswith("#"):
            continue
        elif not line.strip():  # i.e. if line is blank
            continue
        else:
            line_count += 1
    
    return line_count


if __name__ == "__main__":
    main()
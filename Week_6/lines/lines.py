# CS50 assignment: in a file called lines.py, implement a program that expects exactly one 
# command-line argument, the name (or path) of a Python file, and outputs the number of lines 
# of code in that file, excluding comments and blank lines. If the user does not specify exactly 
# one command-line argument, or if the specified file’s name does not end in .py, or if the 
# specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring 
# should not be considered a comment.) Assume that any line that only contains whitespace is blank.

import sys

def main():
    filename = sys.argv[0]
    line_count = lines(filename)
    print(f"Number of lines in {filename}: {line_count}")

def lines(filename):
    
    line_count = 0
    suffix = sys.argv[0].rpartition('.')[-1]
    
    if suffix != "py":
        sys.exit("Not a python filename")

    elif (len(sys.argv)) != 1:
       sys.exit("Too many command-line arguments")

    else:
        try:
            with open(sys.argv[0]) as file:
                for line in file:
                    if line.lstrip() == "#":
                        pass
                    elif line in ["\n", "\t", "\r\n", "\n\r", "\t\n", "\t\r", "\t\n\r", "\t\r\n"]: # i.e. if line is blank
                        pass
                    else:
                        line_count += 1
        except FileNotFoundError ("File does not exist"):
            sys.exit()

    return line_count


if __name__ == "__main__":
    main()
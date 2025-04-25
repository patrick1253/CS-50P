# CS50 assignment: In a file called scourgify.py, implement a program that:

#    Expects the user to provide two command-line arguments:
#        the name of an existing CSV file to read as input, whose columns are assumed to be, in 
#           order, name and house, and the name of a new CSV to write as output, whose columns 
#           should be, in order, first, last, and house.
#    Converts that input to that output, splitting each name into a first name and last name. Assume 
#           that each student will have both a first name and last name.

# If the user does not provide exactly two command-line arguments, or if the first cannot be read, 
# the program should exit via sys.exit with an error message.

import sys
import csv

def main():
    filename = sys.argv[1:]
    
    if len(filename) < 2:
        sys.exit("Too few CLI arguments")

    if len(filename) > 2:
        sys.exit("Too many CLI arguments")

    suffix = (filename[0].split('.')[-1])
          
    if suffix != "csv":
        sys.exit(f"\"{filename[0]}\" is not a CSV filename")

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    students = read_csv(input_file)
    write_csv(output_file, students)


def read_csv(input_file):
    students = []

    try:
        file = open(input_file, "r")
    except FileNotFoundError:
        sys.exit(f"\"{input_file}\" does not exist")
    else:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name'].split(',')
                students.append({"first":name[1], "last":name[0], "house":row['house']})
    return students


def write_csv(output_file, students):
    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames = students[0].keys())
        writer.writeheader()
        writer.writerows(students)
    return output_file


if __name__ == "__main__":
    main()
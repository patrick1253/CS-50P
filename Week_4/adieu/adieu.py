# CS50 assignment: In a file called adieu.py, implement a program that prompts 
# the user for names, one per line, until the user inputs control-d. Assume that 
# the user will input at least one name. Then bid adieu to those names, separating 
# two names with one and, three names with two commas and one and, and names with
# commas and one and, as in the below:

#    Adieu, adieu, to Liesl
#    Adieu, adieu, to Liesl and Friedrich
#    Adieu, adieu, to Liesl, Friedrich, and Louisa

import inflect
p = inflect.engine()

def main():
    print(list_names())
    #print(list_names_alt1())

def list_names():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break
    if len(names) > 1:
        names[-1] = ("and " + names[-1])
    names = ', '.join(names)
    return (f"Adieu, adieu, to {names}")
    
# Alternative way, by importing "inflect":

def list_names_alt1():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break
    names = p.join((names), final_sep = ",")
    return (f"Adieu, adieu, to {names}")

if __name__ == "__main__":
    main()

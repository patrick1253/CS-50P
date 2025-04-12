# CS50 assignment: implement a program that prompts the user for an arithmetic expression 
# and then calculates and outputs the result as a floating-point value formatted to one 
# decimal place. Assume that the user’s input will be formatted as x y z, with one space 
# between x and y and one space between y and z, wherein:

#    x is an integer
#    y is +, -, *, or /
#    z is an integer

# For instance, if the user inputs 1 + 1, your program should output 2.0. 
# 
# Assume that, if y is /, then z will not be 0.

def main():
    formula = input("Type a math formula here, consisting of an iteger, a space, an operator, " \
    "a space, and an integer: ").split(' ')
    print(interpret(formula))
    print(alt_interpret(formula))

def interpret(f):
    x = int(f[0])
    y = f[1]
    z = int(f[2])
    return(float(eval(f"{x} {y} {z}")))

# The above works, but per StackOverflow "eval" is considered unsafe.  
# Here is an alternative, using "import operator":

import operator

allowed_operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

def alt_interpret(f):
    x = int(f[0])
    y = f[1]
    z = int(f[2])
    result = allowed_operators[y](x,z)
    return float(result)

main()
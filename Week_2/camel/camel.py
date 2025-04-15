# CS50 assignment: implement a program that prompts the user for the name of a 
# variable in camel case and outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.

def main():
    snake_output(input("Type a variable name here in camelCase: "))
    #print(''.join(snake))
    output = ''.join(snake)
    print(output)

def snake_output(camel):
    for char in camel:
        if char.islower():
            snake.append(char)
        else:
            snake.append('_' + char.lower())
    return snake

snake = []

main() 






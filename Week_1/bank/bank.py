# CS50 assignment: In a file called bank.py, implement a program that prompts the user 
# for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts 
# with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading 
# whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main(): 
    greeting = input("Please type a greeting: ").strip().lower()
    print(hello(greeting))

def hello(g):
    if "hello" in g:
        return("$0")
    elif g[0] =="h":
        return("$20")
    return ("$100")

main()


#CS50P assignment: implement a program in Python that prompts the user for input and then 
# outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged.

def main():
    shout = input("Say something in all caps: ").lower()
    print(shout)

main()

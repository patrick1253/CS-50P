# CS50 assignment: In a file called bank.py, implement a program that prompts the user 
# for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts 
# with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading 
# whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main(): 
    print(f"${hello()}")

def hello():
    greeting = input("Please type a greeting: ").strip().lower()
    
    if "hello" in greeting:
        return int(0)
    elif greeting[0] =="h":
        return int(20)
    return int(100)

if __name__ == "__main__":
    main()


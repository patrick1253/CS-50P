# CS50 assignment: implement a program that prompts the user for the answer to the Great 
# Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or 
# (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    answer = input("What is the answer to life, the universe, and everything? ").strip().lower()
    if is_answer(answer):
        print("yes")
    else:
        print("no")

def is_answer(a):
    list = ["42", "forty-two", "forty two"]
    if a in list:
        return True
    return False


main()
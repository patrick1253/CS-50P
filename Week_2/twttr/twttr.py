# CS50 assignment:  implement a program that prompts the user for a str of 
# text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

def main():
    cut_vowels(input("Type a brief text message: "))
    no_vwl_msg = "".join(no_vowels)
    print(no_vwl_msg)

def cut_vowels(message):
    for char in message:
        if char not in vowels:
            no_vowels.append(char)

vowels = ["a","e","i","o","u","A", "E", "I" "O", "U"]
no_vowels = []

main()
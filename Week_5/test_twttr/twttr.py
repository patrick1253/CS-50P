# CS50 assignment:In a file called twttr.py, reimplement Setting up my twttr 
# from Problem Set 2, restructuring your code per the below, wherein shorten expects 
# a str as input and returns that same str but with all vowels (A, E, I, O, and U) 
# omitted, whether inputted in uppercase or lowercase.

# Then, in a file called test_twttr.py, implement one or more functions that collectively 
# test your implementation of shorten thoroughly, each of whose names should begin with 
# test_ so that you can execute your tests with: "pytest test_twttr.py"

def main():
    word = shorten(input("Type a brief text message: "))
    print(shorten(word))


def shorten(word):
    vowels = ["a","e","i","o","u","A", "E", "I", "O", "U"]
    no_vowels = []

    for char in word:
        if char not in vowels:
            no_vowels.append(char)

    no_vwl_msg = "".join(no_vowels)
    return no_vwl_msg


if __name__ == "__main__":
    main()
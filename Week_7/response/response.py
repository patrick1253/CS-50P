# CS50 assignment: using either validator-collection or validators from PyPI, implement 
# a program that prompts the user for an email address via input and then prints Valid 
# or Invalid, respectively, if the input is a syntatically valid email address. You may 
# not use re. And do not validate whether the email address’s domain name actually exists.

# from validator_collection import validators, checkers, errors
#from validators import email 
import validators

def main():
    email = (input("Email: "))
    print(validate(email))

def validate(email):
    return validators.email(email)

if __name__ == "__main__":
    main()
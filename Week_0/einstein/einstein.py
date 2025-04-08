# CS50 assignment:  implement a program in Python that prompts the user fro a mass as an integer
# (in kilograms) and then outputs the equivalent number of Joules as an integer.  Assume the user
# will imput an integer.

def main():
    mass = input("Input a mass in kg to see its energy equivalent in Joules:")
    joules = int(mass)*(300000000**2)
    print(f"{mass} kilograms is equivalent to {joules} Joules.")

main()
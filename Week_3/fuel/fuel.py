#CS50 assignment: mplement a program that prompts the user for a fraction, 
# formatted as X/Y, wherein each of X and Y is an integer, and then outputs, 
# as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank 
# is essentially empty. And if 99% or more remains, output F instead to 
# indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, 
# instead prompt the user again. (It is not necessary for Y to be 4.) 
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    #fraction = input("Enter a fraction as X/Y, where X > Y and both are integers: ")
    #fraction = convert_fraction()
    print(convert_fraction())

def convert_fraction():
    while True:
        frac = input("Enter a fraction as X/Y, where X > Y and both are integers: ")
        X = frac.split('/')[0]
        Y = frac.split('/')[1]
        
        try: 
            X = int(X)
            Y = int(Y)
        except ValueError:
            print("X and Y must be numbers")
        else:
            try:
                pct = (X/Y)
            except ZeroDivisionError:
                print("Y cannot be zero")
            else:
                if X > Y:
                    print("X must be less than Y") 
                else:
                    break

    if pct < 0.02:
        pct = "E"
    elif pct > 0.98:
        pct = "F"
    else:
        pct = ("{:.0%}".format(pct))
    
    return (pct)

if __name__ == "__main__":
    main()
    
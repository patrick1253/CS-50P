#CS50 assignment: mplement a program that prompts the user for a fraction, 
# formatted as X/Y, wherein each of X and Y is an integer, and then outputs, 
# as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank 
# is essentially empty. And if 99% or more remains, output F instead to 
# indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, 
# instead prompt the user again. (It is not necessary for Y to be 4.) 
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.


#Receives percentage as integer; prints that fraction as a string formatted as a percentage

def main():
    frac = input("Enter a fraction as X/Y, where X > Y and both are integers: ")
    pct = convert(frac)
    print(pct)


# Converts a fraction input as string X/Y to an integer between 0 and 100 and returns that integer.

def convert(frac):
    #while True:
        #frac = input("Enter a fraction as X/Y, where X > Y and both are integers: ")
    X = frac.split('/')[0]
    Y = frac.split('/')[1]
    
    try: 
        X = int(X)
        Y = int(Y)
    except ValueError:
        raise ValueError("X and Y must be integer numbers")
    else:
        try:
            pct = int((X/Y)*100)
        except ZeroDivisionError:
            raise ZeroDivisionError ("Y cannot be zero")
        else:
            if X > Y:
                raise ValueError ("X must be less than Y") 
            else:
                #return(pct)
                return gauge(pct)

def gauge(pct):
    #pct = convert()
    
    try: 
        pct = int(pct)
    except ValueError: 
        raise ValueError("X and Y must be integer numbers")
    
    if pct <= 1:
        pct = "E"
    elif pct >= 99:
        pct = "F"
    else:
        pct = pct/100
        pct = ("{:.0%}".format(pct))
    return(pct)

if __name__ == "__main__":
    main()
    
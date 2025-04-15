# CS50 assignment: In a file called coke.py, implement a program that prompts the 
# user to insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the 
# user is owed. Assume that the user will only input integers, and ignore any integer 
# that isn’t an accepted denomination.

def main():
    change_due()

def insert_coin():
    total = 0
    while total < cost:
        coin = input("Please deposit one 5 cent, 10 cent, or 25 cent coin: ")
        if coin in(accepted_coins):
            total += int(coin)
            if total <= cost:
                print(f"Amount Due: {cost - total}")
        else:
            print(f"Amount Due: {cost - total}")
    return total
    
accepted_coins = ['5', '10', '25']
cost = 50

def change_due():
    total = insert_coin()
    change = total - cost
    print(f"Change Due: {change}")

main()
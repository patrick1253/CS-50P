#CS50 assignment: In a file called grocery.py, implement a 
# program that prompts the user for items, one per line, until 
# the user inputs control-d (which is a common way of ending one’s 
# input to a program). Then output the user’s grocery list in all 
# uppercase, sorted alphabetically by item, prefixing each line 
# with the number of times the user inputted that item. No need to 
# pluralize the items. Treat the user’s input case-insensitively.

def main():
    grocery_list()

def grocery_list():
    list = {}
    
    while True:
        try:
            item = input("Enter item: ").strip().upper()
        except EOFError:
            print()
            break
        else:
            if item in list:
                list.update({item:list[item]+1})
            else:
                list.update({item:1})

    for item in sorted(list):
        print(list[item], item, sep=" ")
    
    '''
    # A second method, but which relies on importing a specific package:

    from collections import Counter

    list = []
    while True:
        try:
            item = input("Enter item: ").strip().upper()
        except EOFError:
            print()
            break
        else:
            list.append(item)

    count = (Counter(list))
    for key in count:
        print(count[key], key)
    '''
        
if __name__ == "__main__":
    main()
    


    
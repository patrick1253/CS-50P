# AtBS: Chapter 4 "Comma Code"

"""
Takes as an input either a list object or user input (a string of items separated by only one space), and 
returns a comma seaparated string including the word 'and' before the final entry.

:param items: the list object or string to be converted
:type items:  str if input by user, list if set as a list variable
:return: a comma separated string including the word 'and' before the final entry
:rtype: str
"""

spam = ['apples', 'bananas', 'tofu']
spam2 = ['one', 'two', 'three', 'four', 'five']


def main():
    items: str = input("Input list of items separated by one space: ")
    #items = spam2
    print(convert_list(items))
    
def convert_list(items):
    if type(items) == str:
        items = items.split()
    else:
        items = *

    match len(items):
        case 0:
            return "List is empty"
        case 1:
            return f"{items[0]}"
        case 2:
            return f"{items[0]} and {items[1]}"
        case _:
            last = items[-1]
            del items[-1]
            return f"{', '.join(items)}, and {last}"
            

if __name__ == "__main__":
    main()

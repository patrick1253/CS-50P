# CS50 assignment: mplement a function called convert that accepts a 
# str as input and returns that same input with any :) converted to 🙂 
# (otherwise known as a slightly smiling face) and any :( converted to 🙁 
# (otherwise known as a slightly frowning face). All other # text should be returned unchanged.

# this worked, but was not elegant:
# emote = input("Type a message that includes an old-school emoticon: ").replace(':)', '🙂').replace(':(', '🙁')

#So I replaced it with a list, instead of chaining the .replace() methods:

def main():
    # emote = input("Type a message that includes an old-school emoticon: ").replace(':)', '🙂').replace(':(', '🙁')
    emote = input("Type a message that includes an old-school emoticon: ")
    for old, new in replacements:
        emote = emote.replace(old, new)
    print(emote)

replacements = [
    (':)', '🙂'),
    (':(', '🙁'),
]

main()
                                                                            
                                                                                   
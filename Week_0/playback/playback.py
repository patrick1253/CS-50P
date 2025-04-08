# CS-50P assignment:In a file called playback.py, implement a program in Python that 
# prompts the user for input and then outputs that same input, replacing each space 
# with ... (i.e., three periods).

def main():
    lecture = input("Type a short phrase:").replace(' ', '...')
    print(lecture)

main()

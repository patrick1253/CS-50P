# AtBS Chapter 5 assignment:  validate whether the composition of the chess board is valid

import re
import sys
import pprint

def main():
    theBoard = {'1a':'wrook', '1b':'wknight', '2a': 'wpawn', '2b':'wpawn', '7b':'bqueen', '8z':'bqueen', '9z':'wqueen'}
    squares = list(theBoard.keys())
    pieces = list(theBoard.values())

    valid_squares(squares)
    valid_pieces(pieces)
    
def valid_squares(squares):
    #print(squares)
    
    for i in range(len(squares)):
        square = squares[i]
        #print(square)

        matches = re.search(r"^[1-8]{1}[a-h]{1}$", square)
        if not matches:
            print(f"{square} is an invalid square")
            #sys.exit("Invalid square")

def valid_pieces(pieces):
    allowed_pieces = {'wrook':2, 'wknight':2, 'wbishop':2, 'wking':1, 'wqueen':1, 'wpawn':8, \
                      'brook':2, 'bknight':2, 'bbishop':2, 'bking':1, 'bqueen':1, 'bpawn':8}
    pieces_count = {}

    for piece in pieces:
        pieces_count.setdefault(piece, 0)
        pieces_count[piece] = pieces_count[piece] + 1
        
    for piece, count in pieces_count.items():
        if (count > allowed_pieces[piece]):
            #print(f"Piece: {piece}, Count: {count}, ", end="")
            #print(f"Pieces allowed: {allowed_pieces[piece]}")
            print(f"Invalid number of pieces: there are {count} {piece} but only {allowed_pieces[piece]} {piece} are allowed.")
            #sys.exit("Invalid number of pieces")

    
    #pprint.pprint(pieces_count)
    #test change for commit 


if __name__ == "__main__":
    main()
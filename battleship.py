from random import randint

#Board for ship locations
hidden_board = [[" "] * 8 for x in range(8)]
#Board for displaying hits and misses
guess_board = [[" "] * 8 for i in range(8)]

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3, 
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
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

#computer creates 7 ships
def create_ships(board):
    for ship in range(7):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

        def get_ship_location():
            row = input("Enter what row you would like to hit: ").upper()
            while row not in "12345678":
                print('Not a valid choice, please try selecting another row between 1-8: ').upper()
                row = input("Enter what row you would like to hit: ").upper()
                column = input("Enter what column you would like to hit: ").upper()
                while column not in "ABCDEFGH":
                    print('Not a valid choice, please try selecting another column between A-H: ')
                    column = input("Enter what column you would like to hit: ").upper()
                    return int(row) - 1, letters_to_numbers[column]


#check if ships are hit
def count_ships_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    create_ships(hidden_board)
    turns = 10
    while turns > 0:
        print('Guess a ship location')
        print_board(guess_board)
        row, column = get_ship_location()
        if guess_board[row][column] == "-":
            print('You guessed that location already, try hitting a different location')
        elif hidden_board[row][column] == "X":
            print("Hit")
            guess_board[row][column] == "X"
            turns -= 1
        else:
            print('You missed').upper()
            guess_board[row][column] == "-"
            turns -= 1
        if count_ships_hit(guess_board) == 7:
            print('You win').upper()
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")
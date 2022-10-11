from random import randint

#Board for holding ship locations
hidden_board = [[' '] * 8 for i in range(8)]
# Board for displaying hits and misses
guess_board = [[' '] * 8 for i in range(8)]
#Convert letter inputs to numbers
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    """
    Print the game board to the console
    """
    print('  A B C D E F G H')
    print('  +-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))
        row_number += 1

def create_ships(board):
    """
    Create and place 5 ships on the board
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    """
    Get user input for ship location guesses
    Upper method used to convert input to match dictionary key
    """
    row = input('Enter the row of the ship: ')
    while row not in '12345678' or len(row) == 0:
        print('Invalid input, please enter a number 1-8')
        row = input('Enter the row of the ship: ')
    column = input("Enter the column of the ship: ").upper()
    while column not in 'ABCDEFGH' or len(column) == 0:
        print('Invalid input, please enter a letter A-H')
        column = input('Enter the column of the ship: ').upper()
    return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    """
    Check for number of hit ships
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def turns():
    turns = input("Enter the number of turns you want to start with 1-10: ")
    while turns not in "12345678910" or len(turns) == 0:
        print('Invalid input, please enter a number 1-10')
        turns = input("Enter the number of turns you want to start with 1-10: ")
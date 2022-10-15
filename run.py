from random import randint

#Board for holding ship locations
player_board = [[' '] * 8 for i in range(8)]
computer_board = [[' '] * 8 for i in range(8)]
# Board for displaying hits and misses
player_guess_board = [[' '] * 8 for i in range(8)]
computer_guess_board = [[' '] * 8 for i in range(8)]
#Convert letter inputs to numbers
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def get_rules():
    print('The rules:')
    print('Choose the number of turns you want to start with, the more turns the easier the game')
    print("When prompted, enter the coordinates of where you think you're opponents battleship is to shoot at it")
    print('O = Miss and X = Hit')
    print('When all of either you or your opponents battleships are sunk, the game ends')
    print('Be mindful of how many turns you have remaining, if you fail to sink all of the opponents battleships before you run out of turns, you lose')
    play = input('Press the enter key to start the game!')
    while play in '':
        main()

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

def determine_turns():
    """
    Determine the starting number of turns
    """
    global turns
    print("Enter the number of turns you want to start with 1-10: ")
    turns = input()
    while turns not in '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40' or len(turns) == 0:
        print('Invalid input, please enter a number 1-10')
        print("Enter the number of turns you want to start with 1-10: ")
        turns = input()
    turns = int(turns)

def play_again():
    """
    Play the game again or exit program on user input
    """
    play_again = input('Would you like to play again? Type yes or no then press enter: ')
    while True:
        if play_again == 'yes':
            welcome()
        elif play_again == 'no':
            break
        else:
            print('Invalid input')
            play_again = input('Would you like to play again? Type yes or no then press enter: ')


def main():
    """
    Main function for playing the game
    """
    create_ships(computer_board)
    determine_turns()
    global turns
    while turns > 0:
        print('Guess a battleship location')
        print_board(player_guess_board)
        row, column = get_ship_location()
        if player_guess_board[row][column] == "O":
            print("You already guessed that location.")
        elif computer_board[row][column] == "X":
            print("You hit a battleship!")
            player_guess_board[row][column] = "X" 
            turns -= 1  
        else:
            print("Sorry, you missed.")
            player_guess_board[row][column] = "O"   
            turns -= 1     
        if count_hit_ships(player_guess_board) == 5:
            print("Congratulations, you sank all of the computer's battleships!")
            play_again()
        print(f"You have {turns} turns left")
        if turns == 0:
            print("Sorry, you have no turns left, Game Over.")
            play_again()

def welcome():
    """
    Welcome message displays on program load
    Gives option to show rules or play game
    """
    print('Welcome to Battleships!')
    print(r"""
              |    |    |
             )_)  )_)  )_)
            )___))___))___)\
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
    """)
    start = input('Press enter to play the game or type rules and press enter to see the rules: ')
    if start not in 'rules' or len(start) == 0:
        main()
    else:
        get_rules()

welcome()
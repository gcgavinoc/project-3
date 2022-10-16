from random import randint
import sys

# Player and Computer boards for holding ship locations
player_board = [[' '] * 8 for i in range(8)]
computer_board = [[' '] * 8 for i in range(8)]
# Player and Computer boards for displaying hits and misses
player_guess_board = [[' '] * 8 for i in range(8)]
computer_guess_board = [[' '] * 8 for i in range(8)]
# Convert letter inputs to numbers
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                      'E': 4, 'F': 5, 'G': 6, 'H': 7}
# Convert number from randint to letters
numbers_to_letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D',
                      4: 'E', 5: 'F', 6: 'G', 7: 'H'}


def get_rules():
    """
    Print game rules to the console
    and play game on user pressing enter key
    """
    print('The rules:')
    print(
          '- Choose the number of turns you want'
          ' to start with,\nthe more turns the easier the game.'
         )
    print(
          '- First, when prompted, enter the coordinates\nof where you want to'
          ' place your ships, you and your opponent have 5 ships each.'
         )
    print(
          "- Then, when prompted, enter the coordinates of where you think"
          " you're\nopponents battleship is to shoot at it."
         )
    print('- Hit = X and Miss = O')
    print(
          '- When all of either you or your opponents battleships are sunk,'
          ' the game ends.'
         )
    print(
          '- Be mindful of how many turns you have remaining,\nif you fail to'
          ' sink all of the opponents battleships\nbefore you run out'
          ' of turns, you lose.\n'
         )
    play = input('Press the enter key to start the game!')
    while play in '':
        main()


def print_board(board):
    """
    Print the game board to the console.
    """
    print('  A B C D E F G H')
    print('  +-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))
        row_number += 1


def create_computer_ships(board):
    """
    Create and place 5 ships on the board
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = 'X'


def place_player_ships(board):
    """
    Place ships on the player board on user input.
    """
    for ship in range(5):
        ship_row = input('Please enter the row number 1-8 of your ship: ')
        while ship_row not in '12345678' or len(ship_row) == 0:
            print('Invalid input, please enter a number 1-8')
            ship_row = input('Please enter the row of your ship: ')
        ship_column = input(
                            'Please enter the column letter A-H of'
                            ' your ship: '
                           ).upper()
        while ship_column not in 'ABCDEFGH' or len(ship_column) == 0:
            print('Invalid input, please enter a letter A-H')
            ship_column = input(
                                'Please enter the column'
                                ' of your ship: '
                               ).upper()
        ship_row = int(ship_row) - 1
        ship_column = letters_to_numbers[ship_column]
        while board[ship_row][ship_column] == 'X':
            print(
                  'You have already placed a ship there, please enter'
                  ' different coordinates'
                 )
            ship_row, ship_column = input(
                                          'Please enter the row of your'
                                          ' ship: '
                                         ), input(
                                                  'Please enter the'
                                                  ' column of your ship: '
                                                 ).upper()
            ship_row = int(ship_row) - 1
            ship_column = letters_to_numbers[ship_column]
        board[ship_row][ship_column] = 'X'
        print_board(player_board)


def get_ship_location():
    """
    Get user input for ship location guesses.
    upper method used to convert input to match 
    letters_to_numbers dictionary key.
    """
    row = input('Enter the row number 1-8 of the ship: ')
    while row not in '12345678' or len(row) == 0:
        print('Invalid input, please enter a number 1-8')
        row = input('Enter the row of the ship: ')
    column = input("Enter the column letter A-H of the ship: ").upper()
    while column not in 'ABCDEFGH' or len(column) == 0:
        print('Invalid input, please enter a letter A-H')
        column = input('Enter the column of the ship: ').upper()
    return int(row) - 1, letters_to_numbers[column]


def computer_turn():
    """
    Computer guesses ship location on player board
    """
    row, column = randint(0, 7), randint(0, 7)
    return row, column


def count_hit_ships(board):
    """
    Check for number of hit ships.
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count
    print(count)


def determine_turns():
    """
    Determine the starting number of turns.
    """
    global turns
    print("Enter the number of turns you want to start with 1-60: ")
    turns = input()
    while turns not in '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,\
22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,\
40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,\
58,59,60' or len(turns) == 0:
        print('Invalid input, please enter a number 1-60')
        print("Enter the number of turns you want to start with 1-60: ")
        turns = input()
    turns = int(turns)


def clear_boards(board):
    """
    Clears marks and misses from game boards
    """
    for row in board:
        for column in row:
            if column == 'X':
                column = ' '
            elif column == 'O':
                column = ' '


def play_again():
    """
    Play the game again or exit program on user input.
    """
    play_again = input(
        'Would you like to play again? Type yes or no then'
        ' press enter: '
    )
    while True:
        if play_again == 'yes':
            clear_boards(player_board)
            clear_boards(computer_board)
            clear_boards(player_guess_board)
            clear_boards(computer_guess_board)
            welcome()
        elif play_again == 'no':
            sys.exit('Thank you for playing!')
        else:
            print('Invalid input')
            play_again = input(
                'Would you like to play again? Type yes or no'
                ' then press enter: '
            )


def main():
    """
    Main function for playing the game.
    """
    determine_turns()
    create_computer_ships(computer_board)
    place_player_ships(player_board)
    global turns
    while turns > 0:
        print('++ Computer Board ++')
        print_board(computer_guess_board)
        print(' ++ Player Board ++')
        print_board(player_guess_board)
        print('Guess a battleship location')
        row, column = get_ship_location()
        while True:
            if player_guess_board[row][column] == 'O':
                print('You already guessed that location.')
                row, column = get_ship_location()
            elif player_guess_board[row][column] == 'X':
                print('You already guessed that location.')
                row, column = get_ship_location()
            else:
                break
        if computer_board[row][column] == 'X':
            print('You hit a battleship!')
            player_guess_board[row][column] = 'X'
            turns -= 1  
        else:
            print('Sorry, you missed.')
            player_guess_board[row][column] = 'O'  
            turns -= 1     
        if count_hit_ships(player_guess_board) == 5:
            print(
                  "Congratulations, you sank all of the computer's"
                  " battleships!"
                 )
            play_again()
        computer_row, computer_column = computer_turn()
        while True:
            if computer_guess_board[computer_row][computer_column] == 'O':
                computer_row, computer_column = computer_turn()
            elif computer_guess_board[computer_row][computer_column] == 'X':
                computer_row, computer_column = computer_turn()
            else:
                break
        if player_board[computer_row][computer_column] == 'X':
            print('The computer guessed:')
            print(int(computer_row) + 1, numbers_to_letters[computer_column])
            print('The computer hit one of your Battleships!')
            computer_guess_board[computer_row][computer_column] = 'X'  
        else:
            print('The computer guessed:')
            print(int(computer_row) + 1, numbers_to_letters[computer_column])
            print('The computer missed')
            computer_guess_board[computer_row][computer_column] = 'O'    
        if count_hit_ships(computer_guess_board) == 5:
            print('The computer sank all of your Battleships, you lose!')
            play_again()
        print(f'You have {turns} turns left')
        if turns == 0:
            print('Sorry, you have no turns left, Game Over.')
            play_again()


def welcome():
    """
    Welcome message displays on program load.
    Gives option to show rules or play game.
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
    start = input(
                  'Press enter to play the game\nor type rules and press enter'
                  ' to see the rules: \n'
                 )
    if start not in 'rules' or len(start) == 0:
        main()
    else:
        get_rules()


welcome()

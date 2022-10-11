from random import randint

#Board for holding ship locations
hidden_board = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
guess_board = [[" "] * 8 for i in range(8)]

def print_board(board):
    """
    Print the game board to the console
    """
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

print_board(hidden_board)
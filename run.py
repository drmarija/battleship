# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint

board = []

for x in range(5):
    board.append(["-"] * 5)


def print_board(board):
    """
    using zip function to loop over the letters
    and row data in parallel
    """

    print(" ", "".join("12345"))
    for letter, row in zip("ABCDE", board):
        print(letter, "".join(row))


# Starting the game and printing the board
print("Ready to have some fun? Let's play Battleship game!")
print("Guess the place of the ship, btw 0 and 4 for row and column!")
print("You have 6 attempts to complete the game.")
print("Let's start!")

print_board(board)

# Defining the ship place on the board
def random_row(board):
    return randint(0, len(board) - 1)  
def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board) 
ship_col = random_col(board)

# Defining the player attempts to guess where the ship is located
attempt = 0
for attempt in range(6):
    print("Attempt"), attempt
    guess_row = int(input("Please, guess the Row: "))
    guess_col = int(input("Please, guess the Column: "))

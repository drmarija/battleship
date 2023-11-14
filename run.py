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
print("Guess the place of the ship, by guessing the row and column.")
print("You have 6 attempts to complete the game.")
print("Let's start!")

print_board(board)

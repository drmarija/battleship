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

    print(" ", "".join("01234"))
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

for attempt in range(6):
    print("Attempt"), attempt
    guess_row = int(input("Please, guess the Row: "))
    guess_col = int(input("Please, guess the Column: "))

    """
    If the player guess the ship location,
    the game is over
    """
    if guess_row == ship_row and guess_col == ship_col:
        print("Wow, congrats! You sunk my battleship!")
        break
    else:
        """
        Warning the player the guess is out of the board
        and that the guess hit the same place again
        """
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 
           or guess_col > 4):
            print("Oh, you missed the whole board, please try again!")

        elif (board[guess_row][guess_col] == "X"):
            print("You have already guessed that place!")

        else:
            """
            If the guess is wrong, mark with X and
            continue the game
            """
            print("You have missed my battleship!")   
            board[guess_row][guess_col] = "X"

        # print attempt and board again
        print("Attempt" + " " + str(attempt+1) + " " + "out of 6 possible.")   
        print_board(board) 

# If player has used all 6 attempts, then the game is over
if attempt == 5:
    print("Game over! Sorry, out of attempts, better luck next time.")  
    attempt =+1
    print_board(board)     

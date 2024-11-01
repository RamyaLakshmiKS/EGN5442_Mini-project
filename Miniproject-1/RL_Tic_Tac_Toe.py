"""
Name: Ramya Lakshmi Kuppa Sundararajan
UFID: 75288215
Date: 21/09/2024

This file executes the Game Tic Tac Toe played by the users on a same keyboard.
New Game starts with player X and switches between players turn. 
Asks the players input and fills up the game board.
Notifies the player if the input is invalid or if the position is already filled.
Declares whether the game has a winner or if it results in a draw.
Asks the player to repeat if yes then starts a new game by resetting the game board.

"""
# Defining a function with empty List of lists of size 3x3
def initialize_board():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board

# Creation of a game board
def print_board(board):
    print("-------------------")  # Separates each row
    print("| R\C | 0 | 1 | 2 |")  # Heading for the columns
    print("-------------------")
    for i in range(3):
        row = f"|  {i}  | "  # Heading for the rows
        for empty_cell in board[i]:
            row += empty_cell + " | "  # Add each cell to the row
        print(row)  # Print the constructed row
        print("-------------------")

# Defining function for players input
def player_input(player):
    print(f"{player}'s turn.")   # Display which player's turn
    print(f"Where do you want your {player} placed?")    # Questions the player
    player_input = input("Please enter row number and column number separated by a comma.\n")
    try:
        row, column = player_input.split(",")  # Splits the input as row and column
        row = int(row)                         # Converts to integer
        column = int(column)
        return row, column                     # Return row and column as integer
    except:
        # If the user enters something like 0, 'a' (non integer character) etc:- , I am returning a invalid choice which will be handled later in the code
        return -1, -1

# Defining function for validating the players input
def validate_input(row, column, board):
    no_of_rows = len(board)
    no_of_cols = len(board[0])
    # Handles the case where the user has entered input with no commas or a alphabet input
    if row < 0 or column < 0:
        print("Invalid entry: try again.")
        print("Row & column numbers must be separated by comma.\n")
        return False
    if row not in range(no_of_rows) or column not in range(no_of_cols):  # Checks if input out of board
        print(f"You have entered row #{row}\n\t  and column #{column}")
        print("Invalid entry: try again.")
        print("Row & column numbers must be either 0, 1, or 2.\n")
        return False
    elif board[row][column] != " ":  # Checks whether the cell is empty
        print(f"You have entered row #{row}\n\t  and column #{column}")
        print("That cell is already taken.")
        print("Please make another selection.\n")
        return False
    else:
        return True

# Defining function for making the move in board
def make_move(row, column, player, board):
    board[row][column] = player
    print(f"You have entered row #{row}\n\t  and column #{column}")
    print("Thank you for your selection.")

def check_horizontal_win(board, player):
    no_of_rows = len(board)
    no_of_cols = len(board[0])
    for row in range(no_of_rows):
        # Keep track of number of times player is seen in the row
        count = 0
        for col in range(no_of_cols):
            # Current iteration element in the board
            curr = board[row][col]
            if curr == player:
                count += 1
        if count == no_of_cols:
            return True
            # This means the player has filled all cols in this row, so X/O won the game
    return False

def check_vertical_win(board, player):
    no_of_rows = len(board)
    no_of_cols = len(board[0])
    for col in range(no_of_cols):
        # Keep track of number of times player is seen in the col
        count = 0
        for row in range(no_of_rows):
            curr = board[row][col]
            if curr == player:
                count += 1
        if count == no_of_rows:
            # This means the player has filled all rows in this col, so X/O won the game
            return True
    return False

def check_diagonal_win(board, player):
    no_of_rows = len(board)
    # Track the count from top left to bottom right
    count_tl_br = 0
    # Track the count from top right to bottom left
    count_tr_bl = 0
    for i in range(no_of_rows):
        # This iterates like (0,0), (1,1), (2,2)
        if board[i][i] == player:
            count_tl_br += 1
        # This iterates like (0,2), (1,1), (2,0)
        if board[i][no_of_rows - 1 - i] == player:
            count_tr_bl += 1
    # This means one of the two diagonals is full, so X/O won.
    if count_tl_br == no_of_rows or count_tr_bl == no_of_rows:
        return True
    return False

# Defining function to check if the game has winner
def check_winner(board, player):
    return (check_diagonal_win(board, player)
        or check_horizontal_win(board, player)
        or check_vertical_win(board, player))

# Defining a function to check if the game board is full
def board_full(board):
    for cell in board:  # Loop starts
        if " " in cell:  # Checks if the cell is empty
            return False
    return True

# Defining a main function where the game process starts
def main():
    repeat = "Yes"
    while repeat[0].lower() == "y":  # Loop begins
        board = initialize_board()   # Initialize the game board
        current_player = "X"         # Starts with player X
        print("New Game: X goes first. \n")
        print_board(board)  # Displays the game board
        print()

        while True:   # Loop runs when its true
            row, column = player_input(current_player)  # Gets player input

            if validate_input(row, column, board):  # Runs if the input is valid
                make_move(row, column, current_player, board)
                print_board(board)  # Update the board
                print()

                if check_winner(board, current_player):  # Checks if there is a winner and prints the output accordingly
                    print(f"{current_player} IS THE WINNER!!!") # Announce the winner
                    break  # Exits the loop

                if board_full(board):  # Checks if the board's full and prints the output accordingly
                    print("DRAW! NOBODY WINS")
                    break  # Exits the loop

                # Switches between players
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"

        # Asks player if they wanted to start a new game
        repeat = input("Another game? Enter Y or y for yes.\n")
    print("Thank you for playing!")

# Calling the function
if __name__ == "__main__":
    main()

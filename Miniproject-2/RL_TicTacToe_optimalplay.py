"""
Name: Ramya Lakshmi Kuppa Sundararajan
UFID: 75288215
Date: 27/10/2024

This file runs a Tic-Tac-Toe game between a Human and an AI. Each game starts with the Human as player X, 
alternating turns between Human and AI. The program requests inputs from both players, updates the game board, 
and alerts the player if an input is invalid or if a position is already occupied. It announces a winner or 
a draw when applicable and prompts the Human to play again. If yes, it resets the board for a new game.

In this version, I've kept the core of my Mini Project 1 code intact, modifying only where necessary.

"""

# Imported SVM model from tic tac toe multi class classification
import pandas as pd
file_path = r'E:\UF MSADS\SEM 1\Programming for DS\Mini project\svm_tictactoe_model.pkl'
svm_model = pd.read_pickle(file_path)

# Defining a function with empty List of lists of size 3x3
def initialize_board():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board

# Creation of a game board
def print_board(board):
    print("-------------------")
    print("| R\C | 0 | 1 | 2 |")
    print("-------------------")
    for i in range(3):
        row = f"|  {i}  | "
        for empty_cell in board[i]:
            row += empty_cell + " | "
        print(row)
        print("-------------------")

# Defining function for players input
def player_input(player):
    print(f"{player}'s turn.")    # Display which player's turn
    print(f"Where do you want your {player} placed?")     # Questions the player
    player_input = input("Please enter row number and column number separated by a comma.\n")
    try:
        row, column = player_input.split(",")    # Splits the input as row and column
        row = int(row)
        column = int(column)         # Converts to integer
        return row, column           # Return row and column as integer
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
        print("Row & column numbers must be separated by a comma.\n")
        return False
    if row not in range(no_of_rows) or column not in range(no_of_cols):    # Checks if input out of board 
        print(f"You have entered row #{row}\n\t  and column #{column}")
        print("Invalid entry: try again.")
        print("Row & column numbers must be either 0, 1, or 2.\n")
        return False
    elif board[row][column] != " ":     # Checks whether the cell is empty
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

# Check for a win (horizontal, vertical, diagonal)
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

# Defining a function for AI to select its move
def ai_move(board):
    # Convert the board state to a list for the model
    flat_board = []
    for row in board:
        for cell in row:
            flat_board.append(cell)
    
    # Input for the model: X as +1, O as -1, and empty as 0
    input_features = []
    for cell in flat_board:
        if cell == 'X':
            input_features.append(1)
        elif cell == 'O':
            input_features.append(-1)
        else:
            input_features.append(0)
    
    # Predicting the best move for the AI using the imported SVM model
    best_move_index = svm_model.predict([input_features])[0]
    
    # Converts the index back to row and column
    row = best_move_index // 3
    col = best_move_index % 3
    return row, col

# Defining a main function where the game process starts
def main():
    # first initializes a variable to repeat the game
    repeat = "Yes"
    while repeat[0].lower() == "y":    # Loop begins
        board = initialize_board()     # Initialize the game board
        current_player = "X"           # Starts with player X
        print("New Game: X goes first.\n")
        print_board(board)     # Displays the game board
        print()

        while True:     # Loop runs when its true
            if current_player == "X":   # Player's turn
                row, column = player_input(current_player)    # Gets player input
            else:
                print("O's turn.")   # AI's turn
                row, column = ai_move(board)     # Gets AI's input

            if validate_input(row, column, board):      # Runs if the input is valid
                make_move(row, column, current_player, board)
                print_board(board)     # Update the board
                print()

                if check_winner(board, current_player):   # Checks if there is a winner and prints the output accordingly
                    print(f"{current_player} IS THE WINNER!!!")    # Announce the winner
                    break    # Exits the loop

                if board_full(board):   # Checks if the board's full and prints the output accordingly
                    print("DRAW! NOBODY WINS")   
                    break    # Exits the loop

                # Switch between player "X" and AI "O"
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"

        # Asks player if they wanted to start a new game
        repeat = input("Another game? Enter Y or y for yes.\n")
    print("Thank you for playing!")

# Calling the main function
if __name__ == "__main__":
    main()

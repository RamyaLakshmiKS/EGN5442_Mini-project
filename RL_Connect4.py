"""
Name: Ramya Lakshmi Kuppa Sundararajan
UFID: 75288215
Date: 28/09/2024

This file executes the Game Connect4 played by the users on a same keyboard.
New Game starts with player X and switches between players turn.
Displays the available positions for each players turn and updates accordingly. 
Asks the players input and fills up the game board.
Notifies the player if the input is invalid or if the position is filled.
Declares whether the game has a winner or if it results in a draw.
Asks the player to repeat if yes then starts a new game by resetting the game board.

"""

# dictionary to access index (Global variable)
column_dict = {'a': 0,
               'b': 1,
               'c': 2,
               'd': 3,
               'e': 4,
               'f': 5,
               'g': 6 }

# Defining a function with empty list of lists of size 6x7 
def initialize_board():
    board = [[" ", " ", " ", " ", " ", " ", " ",],
             [" ", " ", " ", " ", " ", " ", " ",],
             [" ", " ", " ", " ", " ", " ", " ",],
             [" ", " ", " ", " ", " ", " ", " ",],
             [" ", " ", " ", " ", " ", " ", " ",],
             [" ", " ", " ", " ", " ", " ", " ",]]  
    return board

#creation of a game board
def print_board(board):
    for i in [6,5,4,3,2,1]:
        row = f"|  {i}  | "      # Heading for the rows
        for cell in board[i-1]:
            row += cell + " | "  # Add each cell to the row
        print(row)               # Print the constructed row
        print("-------------------------------------")      # Separating each row
    print("| R\C | a | b | c | d | e | f | g |")            # Outside the loop to create column heading at the bottom
    print("-------------------------------------")

# Defining function to display available positions in game board
def available_positions(board):
    no_of_cols = len(board[0])
    no_of_rows = len(board)
    positions = []
    for column in range(no_of_cols):  # starting the loop through each column
        for row in range(no_of_rows):    # Loop through each row
            if board[row][column] == " ":                      # Check if the row and col is empty
                col_letter = list(column_dict.keys())[column]  # Get letter from column_dict
                row_number = row + 1                           # Converts zero index to one
                positions.append(f"{col_letter}{row_number}")  # Adds to the empty list(positions)
                break     # Exits the loop
    return positions

# Defining function for validating the players input
def validate_input(move, board):
        if len(move) != 2:   # Checks if the input is valid
            print("Invalid input: try again.\n")
            return False
    
        column_letter = move[0]
        row_number = move[1]

        if column_letter not in column_dict:      # Checks whether the column letter is present in column dict
            print("Invalid input: try again.\n")
            return False

        # Checks if the row_number is numerical digit
        num = True
        for char in row_number:   # Loop through elements in row number
            if char not in '0123456789':  # Checks if its present in the mentioned string
                num = False
                break     # Exits the loop
        if not num:                               
            print("Invalid input: try again.\n")
            return False  

        row = int(row_number) - 1
        col = column_dict[column_letter]

        if row not in range(6):
            print("Invalid input: try again.\n")
            return False
        
        if board[row][col] != " ":    # Checks if the cell is already taken
            print("That cell is already taken.")
            print("Please make another selection.\n")
            return False
        
        if move not in available_positions(board):   # Checks if the player input is in available positions
            print("Invalid input: try again.\n")
            return False
        return True

# Defining function for players input
def player_input(player, board):
    print(f"{player}'s turn.")   # Display which player's turn
    print(f"Where do you want your {player} placed?")   # Questions the player
    avail_positions = available_positions(board)               # calling the function get_available_positions and assigning it to a variable
    print(f"Available positions are: {avail_positions}\n")     # Displays the available position in the game board
    
    while True:
        move = input("Please enter column-letter and row-number (e.g., a1): ")
        if not validate_input(move, board):
            # ask for input again if input is not valid
            continue

        print("Thank you for your selection.\n")
        return move

# Defining function that updates board
def update_board(board, move, player):
    col = column_dict[move[0]]   # Use column_dict to get column index
    for row in range(6):         # Loop through each row
        if board[row][col] == " ":          # Find the first empty row in the column
            board[row][col] = player        # Place the player's input
            break                           # Exit after placing the input

# Defining function to check if the game has winner
def check_winner(board, player):
    no_of_rows = len(board)
    no_of_cols = len(board[0])
    # Horizontal checking(rows)
    for row in range(no_of_rows):
        for col in range(4):    # check columns 0 - 3 for horizontal wins
            count = 0
            for i in range(4):  # Check the next four cells
                if board[row][col + i] == player:
                    count += 1
                if count == 4:
                    return True
    
    # Vertical checking(columns)
    for col in range(no_of_cols):
        for row in range(3):    # check rows 0 - 2 for vertical wins
            count = 0
            for i in range(4):  # Check the next four cells
                if board[row + i][col] == player:
                    count += 1
                if count == 4:
                    return True

    # Diagonal checking (top-right to bottom left)
    for row in range(3):      # check rows 0 - 2 for bottom-left to top-right diagonals
        for col in range(4):  # check columns 0 - 3 for diagonals
            count = 0
            for i in range(4):  # Check the next four diagonal cells
                if board[row + i][col + i] == player:
                    count += 1
                if count == 4:
                    return True

    # Diagonal checking (top-left to bottom-right)
    for row in range(3, 6):   # check rows 3 - 5 for top-left to bottom-right diagonals
        for col in range(4):  # check columns 0 - 3 for diagonals
            count = 0
            for i in range(4):  # Check the next four diagonal cells
                if board[row - i][col + i] == player:
                    count += 1
                if count == 4:
                    return True
    return False

# Defining a main function where the game process starts
def main():
    repeat = "Yes"
    while repeat[0].lower() == "y": # Loop begins
        board = initialize_board()  # Initialize the game board
        current_player = "X"        # Starts with player X
        print("New Game: X goes first.\n")
        
        while True:  # Loop runs when its true
            print_board(board)  # Display the board
            print()
            play_input = player_input(current_player, board)  # Get the player's input
            update_board(board, play_input, current_player)   # Update the board
            
            # Check if the current player has won
            if check_winner(board, current_player):
                print(f"{current_player} IS THE WINNER!!!")  # Announce the winner
                print_board(board)                           # Show the final board
                break   # Exits the loop
            
            # Switches between players
            if current_player == "X":
                current_player = "O" 
            else:
                current_player = "X"

        # Asks player if they wanted to start a new game
        repeat = input("Another game (y/n)? ")
    print("Thank you for playing!")

# Calling the function
if __name__ == "__main__":
    main()

"""
Name: Ramya Lakshmi Kuppa Sundararajan
UFID: 75288215
Date: 25/10/2024

Tic-Tac-Toe

This program is a simple Tic-Tac-Toe game using classes and objects.
I restructured my Mini Project 1 code to utilize the classes and objects here, 
while maintaining the same functionality as the original. 
    
"""

# define Board class to building the Game Board:

class Board:
     # this constructor initiates the board with empty cells
    def __init__(self):
        self.c = [[" "," "," "],
                  [" "," "," "],
                  [" "," "," "]]
      
    # this method prints the board. Recall that class methods are functions
    def printBoard(self):
        # it first prints the BOARD_HEADER constant
        # BOARD_HEADER constant
        BOARD_HEADER = "-----------------\n|R\\C| 0 | 1 | 2 |\n-----------------"
        print(BOARD_HEADER)
        
        # using a for-loop, it increments through the rows
        for i in range(3):
            row = f"| {i} | "  # Heading for the rows
            for empty_cell in self.c[i]:
                row += empty_cell + " | "  # Add each cell to the row
            print(row)
            print("-----------------")
    
# define Game class to implement the Game Logic:

class Game:
    # the constructor
    def __init__(self):
        self.board = Board()   
        self.turn = 'X'

    # this method switches players 
    def switchPlayer(self):
        if self.turn == 'X':     
            self.turn = 'O' 
        else:
            self.turn = 'X'
    
    # this method validates the user's entry
    def validateEntry(self, row, column):
        no_of_rows = len(self.board.c)
        no_of_cols = len(self.board.c[0])
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
        elif self.board.c[row][column] != " ":  # Checks whether the cell is empty
            print(f"You have entered row #{row}\n\t  and column #{column}")
            print("That cell is already taken.")
            print("Please make another selection.\n")
            return False
        else:
            print(f"You have entered row #{row}\n\t  and column #{column}")
            print("Thank you for your selection.")
            return True

    # this method checks if the board is full
    def checkFull(self):
        for row in self.board.c:    # Loop starts
            if " " in row:      # Checks if empty
                return False
        return True
    
    # this method checks for a winner
    def checkWin(self):
        b = self.board.c    
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != " ":  # Row check
                return True
            if b[0][i] == b[1][i] == b[2][i] != " ":  # Column check
                return True
        if b[0][0] == b[1][1] == b[2][2] != " ":  # Diagonal top-left to bottom-right
            return True
        if b[0][2] == b[1][1] == b[2][0] != " ":  # Diagonal top-right to bottom-left
            return True
        return False
        
    # this method checks if the game has met an end condition by calling checkFull() and checkWin()
    def checkEnd(self):
        # Calling the class method for conditional statement
        if self.checkWin():   
            print(f"{self.turn} IS THE WINNER!!!")
            return True
        if self.checkFull():
            print("DRAW! NOBODY WINS")
            return True
        return False

    # this method runs the tic-tac-toe game
    def playGame(self):
        print("New Game: X goes first.\n")   # Starts with player X
        self.board.printBoard()  # Displays the game board
        print()

        while True:  # Loop runs when its true
            print(f"{self.turn}'s turn.")    # Display which player's turn
            print(f"Where do you want your {self.turn} placed?")    # Questions the player
            player_input = input("Please enter row number and column number separated by a comma.\n")
            try:
                row, column = player_input.split(",")   # Splits the input as row and column
                row = int(row)
                column = int(column)                    # Converts to integer
            except:
                print("Invalid entry: try again.")      # If there is Error in the user input
                print("Row & column numbers must be separated by comma.\n")
                continue
            
            if self.validateEntry(row, column):   # Runs if the input is valid
                self.board.c[row][column] = self.turn
                self.board.printBoard()   # Update the board
                print()

                if self.checkEnd():    # Checks if there is a winner and prints the output accordingly
                    break      # Exits the loop
                
                # Calling the method to switch between players
                self.switchPlayer()

# main function
def main():
    # first initializes a variable to repeat the game
    repeat = "Yes"
    while repeat[0].lower() == 'y':      # Loop begins
        game = Game()
        game.playGame()      # Calling method to run the game
        
        # Asks player if they wanted to start a new game
        repeat = input("Another game? Enter Y or y for yes.\n")
    # goodbye message 
    print("Thank you for playing!")
    
# calling the main function
if __name__ == "__main__":
    main()

# Tic-Tac-Toe Game in Python

# Function to print the current board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Center column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal from top-left to bottom-right
        [2, 4, 6]   # Diagonal from top-right to bottom-left
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (a tie game)
def check_tie(board):
    return " " not in board

# Function for player move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("That spot is already taken! Choose another spot.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Main function to run the game
def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board, current_player)
        print_board(board)
        
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        if check_tie(board):
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()

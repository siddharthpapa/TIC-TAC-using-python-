def print_board(board):
    # Display the board as a 3x3 grid
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move >= 0 and move < 9 and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def check_win(board, player):
    # Define all possible winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    # Check if any winning combination is met
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw(board):
    # A draw occurs if the board is full and there's no winner
    return ' ' not in board

def tic_tac_toe():
    while True:
        board = [' ' for _ in range(9)]  # Initialize the board
        current_player = 'X'  # X always starts
        
        while True:
            print_board(board)
            player_move(board, current_player)
            
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

        # Ask if the players want to play again
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Thanks for playing!")
            break

# Run the game
tic_tac_toe()

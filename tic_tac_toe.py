# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# The 8 ways to get 3 in a row, as board indexes (0-8)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),  # diagonals
]


def display_board(board):
    """Print the 3x3 board. Empty squares show their position number (1-9)."""
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def print_welcome():
    """Print the welcome message and the rules."""
    print("Welcome to a new round of Tic-Tac-Toe!")
    print("Rules: two players take turns placing X or O on the board.")
    print("Pick a square by typing its number (1-9).")
    print("The first player to get 3 in a row (row, column or diagonal) wins!")


def choose_symbols():
    """Ask Player 1 to pick X or O. Return (player1_symbol, player2_symbol)."""
    prompt = "Player 1, do you want to be X or O? "
    symbol = input(prompt).strip().upper()
    while symbol != "X" and symbol != "O":
        print("Please type X or O.")
        symbol = input(prompt).strip().upper()
    if symbol == "X":
        return "X", "O"
    else:
        return "O", "X"


def get_current_player(move_count, player1, player2):
    """Return whose turn it is: player1 on even move counts, player2 on odd."""
    if move_count % 2 == 0:
        return player1
    else:
        return player2


def is_valid_move(board, position_text):
    """Return True if the text is a number from 1 to 9 and that square is still free."""
    if not position_text.isdecimal():
        return False
    position = int(position_text)
    if position < 1 or position > 9:
        return False
    if board[position - 1] == "X" or board[position - 1] == "O":
        return False
    return True


def get_move(board, player):
    """Ask the current player for a square (1-9) until the answer is valid. Return it as an int."""
    prompt = "Player " + player + ", choose a square (1-9): "
    answer = input(prompt).strip()
    while not is_valid_move(board, answer):
        print("Invalid move, try again.")
        answer = input(prompt).strip()
    return int(answer)


def place_move(board, position, symbol):
    """Put the player's symbol on the chosen square (1-9) of the board."""
    index = position - 1
    board[index] = symbol
    print("Player " + symbol + " took square " + str(position) + ".")
    return board


def play_turn(board, player):
    """Play one turn: show the board, ask for a move and place it."""
    print("It's Player " + player + "'s turn.")
    display_board(board)
    position = get_move(board, player)
    place_move(board, position, player)


def check_winner(board, symbol):
    """Return True if the symbol has 3 in a row (row, column or diagonal)."""
    for line in WIN_LINES:
        if all(board[i] == symbol for i in line):
            return True
    return False


def check_draw(move_count):
    """Return True if all 9 squares are filled (only call this after checking for a winner)."""
    if move_count == 9:
        return True
    else:
        return False


def is_game_over(board, symbol, move_count):
    """Check if the last move ended the game. Print the result and return True if so."""
    if check_winner(board, symbol):
        display_board(board)
        print("Player " + symbol + " wins the game!")
        return True
    if check_draw(move_count):
        display_board(board)
        print("It's a draw!")
        return True
    return False


def play_game():
    """Set up a new board and let the two players take turns."""
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print_welcome()
    player1, player2 = choose_symbols()
    move_count = 0
    game_over = False
    while not game_over:
        player = get_current_player(move_count, player1, player2)
        play_turn(board, player)
        move_count += 1
        game_over = is_game_over(board, player, move_count)


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    play_game()

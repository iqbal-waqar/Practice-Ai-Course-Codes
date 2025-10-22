import math
import time

board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(b, player):
    win_combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
    for x, y, z in win_combos:
        if b[x] == b[y] == b[z] == player:
            return True
    return False

def is_draw(b):
    return ' ' not in b

def get_moves(b):
    return [i for i in range(9) if b[i] == ' ']

def evaluate(b):
    if check_winner(b, 'O'):
        return 1    
    elif check_winner(b, 'X'):
        return -1   
    else:
        return 0     

def minimax(b, depth, is_maximizing, max_depth):
    score = evaluate(b)

    if score != 0 or is_draw(b) or depth == max_depth:
        return score

    if is_maximizing:
        best = -math.inf
        for move in get_moves(b):
            b[move] = 'O'
            best = max(best, minimax(b, depth + 1, False, max_depth))
            b[move] = ' '
        return best
    else:
        best = math.inf
        for move in get_moves(b):
            b[move] = 'X'
            best = min(best, minimax(b, depth + 1, True, max_depth))
            b[move] = ' '
        return best

# Iterative Deepening Search (IDS)
def find_best_move(b, time_limit=2):
    start_time = time.time()
    best_move = None
    max_depth = 1

    while time.time() - start_time < time_limit:
        best_score = -math.inf
        current_best = None

        for move in get_moves(b):
            b[move] = 'O'
            score = minimax(b, 0, False, max_depth)
            b[move] = ' '

            if score > best_score:
                best_score = score
                current_best = move

        if current_best is not None:
            best_move = current_best

        max_depth += 1  

    return best_move

def play_game():
    print("Tic-Tac-Toe with Iterative Deepening Search AI")
    print_board()

    while True:
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_move = find_best_move(board, time_limit=2)
        board[ai_move] = 'O'
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

play_game()

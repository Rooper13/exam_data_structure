import copy

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

def minimax(board, depth, maximizing_player):
    winner = check_winner(board)
    if winner:
        return 10 - depth if winner == 'X' else -10 + depth
    elif len(available_moves(board)) == 0:
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in available_moves(board):
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = 'X'
            eval = minimax(new_board, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = 'O'
            eval = minimax(new_board, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for move in available_moves(board):
        new_board = copy.deepcopy(board)
        new_board[move[0]][move[1]] = 'X'
        eval = minimax(new_board, 0, False)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'O'
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Congratulations! {winner} wins!")
            break
        elif len(available_moves(board)) == 0:
            print("It's a tie!")
            break

        # AI's move
        print("AI is making a move...")
        ai_move = get_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"AI wins! Better luck next time.")
            break
        elif len(available_moves(board)) == 0:
            print("It's a tie!")
            break

play_game()

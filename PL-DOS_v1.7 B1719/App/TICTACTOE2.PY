import sys

def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print("\n-------------")

def check_win(board, mark):
    # Check rows, columns, and diagonals
    lines = [board[i] for i in range(3)] + \
            [[board[i][j] for i in range(3)] for j in range(3)] + \
            [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    return any([all([cell == mark for cell in line]) for line in lines])

def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_mark = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        if current_mark == 'X':
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
            except:
                print('谁让你不输入数字的???')
                continue
            try:
                if board[row][col] != ' ':
                    print("Cell already occupied, try again!")
                    continue
                board[row][col] = current_mark
            except:
                print('[X] 你输入了不该输入的东西')
                continue
        else:
            print("AI's turn")
            row, col = find_best_move(board)
            board[row][col] = current_mark
        game_over = check_win(board, current_mark) or is_board_full(board)
        current_mark = 'O' if current_mark == 'X' else 'X'

    print_board(board)
    if check_win(board, 'X'):
        print("You win!")
    elif check_win(board, 'O'):
        print("AI wins!")
    else:
        print("It's a tie!")

tic_tac_toe()
# https://www.codewars.com/kata/525caa5c1bf619d28c000335

def is_solved(board):
    for i in board:
        if i[0] == i[1] == i[2] and i[0] != 0:
            return i[0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    for i in board:
        if 0 in i:
            return -1
    return 0

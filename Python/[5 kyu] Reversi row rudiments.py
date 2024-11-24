# https://www.codewars.com/kata/55aa92a66f9adfb2da00009a

def reversi_row(moves):
    board = ['.'] * 8
    
    flag = True
    
    for move in moves:
        board[move] = '*' if flag else 'O'
        
        for i in range(move - 1, -1, -1):
            if board[i] == '.':
                break
            if board[i] == ('*' if flag  else 'O'):
                for j in range(i + 1, move):
                    board[j] = '*' if flag else 'O'
                break
        
        for i in range(move + 1, 8):
            if board[i] == '.':
                break
            if board[i] == ('*' if flag else 'O'):
                for j in range(move + 1, i):
                    board[j] = '*' if flag else 'O'
                break
        
        flag = not flag
        
    return ''.join(board)
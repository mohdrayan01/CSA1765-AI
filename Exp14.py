# Write the python program to implement Apha & Beta pruning algorithm for gaming 
board = [
    'X','O','X',
    ' ','O',' ',
    ' ',' ','X'
]
def check_winner(player):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    return any(all(board[i] == player for i in p) for p in win)
def alphabeta(board, alpha, beta, is_max):
    if check_winner('X'):
        return -1
    if check_winner('O'):
        return 1
    if ' ' not in board:
        return 0
    if is_max:
        value = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                value = max(value, alphabeta(board, alpha, beta, False))
                board[i] = ' '
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return value
    else:
        value = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                value = min(value, alphabeta(board, alpha, beta, True))
                board[i] = ' '
                beta = min(beta, value)
                if alpha >= beta:
                    break
        return value
result = alphabeta(board, -1000, 1000, True)
if result == 1:
    print("Alpha-Beta Evaluation: 1")
    print("Result: O has a winning strategy.")
elif result == -1:
    print("Alpha-Beta Evaluation: -1")
    print("Result: X has a winning strategy.")
else:
    print("Alpha-Beta Evaluation: 0")
    print("Result: The game will end in a draw.")
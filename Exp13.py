# Write the python program to implement Minimax algorithm for gaming 
board = [
    'X','O','X',
    ' ','O',' ',
    ' ','X',' '
]
def check_winner(player):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    return any(all(board[i] == player for i in p) for p in win)
def minimax(board, is_max):
    if check_winner('X'):
        return -1
    if check_winner('O'):
        return 1
    if ' ' not in board:
        return 0
    if is_max:
        best = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, False))
                board[i] = ' '
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, True))
                board[i] = ' '
        return best
score = minimax(board, True)
print("Board State:", board)
print("Minimax Evaluation Value:", score)
if score == 1:
    print("Interpretation: Player O has a winning strategy.")
elif score == -1:
    print("Interpretation: Player X has a winning strategy.")
else:
    print("Interpretation: The game will end in a draw if both play optimally.")
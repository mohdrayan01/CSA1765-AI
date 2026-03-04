# Write the python program for Tic Tac Toe game 
board = [' ' for _ in range(9)]
def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
def check_winner(player):
    win_positions = [(0,1,2),(3,4,5),(6,7,8),
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8),(2,4,6)]
    return any(all(board[pos] == player for pos in combo) for combo in win_positions)
current_player = 'X'
for turn in range(9):
    print_board()
    move = int(input(f"Player {current_player}, enter position (0-8): "))
    if board[move] == ' ':
        board[move] = current_player
    else:
        print("Position already taken!")
        continue
    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break
    current_player = 'O' if current_player == 'X' else 'X'
else:
    print_board()
    print("It's a draw!")
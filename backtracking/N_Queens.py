def display_board(board):
    for row in board:
        print(row)

def is_safe(board, x, y, n):

    for row in range(x):
        if board[row][y] == 'Q':
            return False
        
    row = x-1
    col = y-1

    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1
     
    row = x-1
    col = y+1
    while row >= 0 and col < n:
        if board[row][col] == 1:
            return False
        row -= 1
        col += 1
    return True

def solve(board, x, n):
    if x>=n:
        return True
    for col in range(n):
        if is_safe(board, x, col, n):
            board[x][col] = 'Q'
            if solve(board, x+1, n):
                return True
            board[x][col] = ' '
    return False

n= int(input("Enter the number of queens: "))
board =[[' ']* n for i in range(n)]

if solve(board, 0, n):
    display_board(board)
else:
    print("Solution does not exist")
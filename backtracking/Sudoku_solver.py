def display(board):
    for row in board:
        print(row)

def is_safe(board, row, col, num):
    # Check if num is in the given row
    if num in board[row]:
        return False
    
    # Check if num is in the given column
    for r in range(9):
        if num == board[r][col]:
            return False
        
    # Check if num is in the 3x3 subgrid
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
            
    return True

def solve(board, row=0, col=0):
    if row == 9:
        return True
    if col == 9:
        return solve(board, row + 1, 0)
    if board[row][col] != 0:
        return solve(board, row, col + 1)
    
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col + 1):
                return True
            board[row][col] = 0
    
    return False

board = [
    [0, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 0, 0, 0]
]

if solve(board):
    display(board)
else:
    print("Solution does not exist")

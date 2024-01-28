def solution(board):
    square=board.copy()
    if board[-1][-1]:
        max_length=1
    else:
        max_length=0
    for row in range(len(board)-2,-1,-1):
        for col in range(len(board[0])-2,-1,-1):
            if board[row][col]==1:
                square[row][col]=min(board[row+1][col],board[row][col+1],board[row+1][col+1])+1
            if max_length<square[row][col]:
                max_length=square[row][col]
    return max_length**2
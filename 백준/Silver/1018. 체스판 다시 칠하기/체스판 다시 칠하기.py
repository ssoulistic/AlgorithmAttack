import sys
m,n=map(int,sys.stdin.readline().split()) # 행,열 수
board=[]
type=["BWBWBWBW","WBWBWBWB"]
for i in range(m):
    board.append(sys.stdin.readline())

paint_min=64
for j in range(m-7):
    for k in range(n-7):
        diff_a=0
        diff_b=0
        for l in range(8):
            for p in range(8):
                if board[j+l][k:k+8][p]!=type[l%2][p]:
                    diff_a+=1
                if board[j+l][k:k+8][p]!=type[(l+1)%2][p]:
                    diff_b+=1
        if paint_min>min(diff_a,diff_b):
            paint_min=min(diff_a,diff_b)
print(paint_min)
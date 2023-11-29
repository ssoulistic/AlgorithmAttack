import sys
# 1. K 크기의 체스판 모양으로 체크 => 몇개를 바꿔야하는지.
# 홀,짝=> 매칭수 체크. 좌측 위가 B냐 W인 경우.
# N 이 행 수(세로길이)
N,M,K=map(int,sys.stdin.readline().split())

# 첫 칸이 블랙 체스판 / 화이트 체스판 -> 그에 따른 바꿔야하는 수 누적

chess_Black=[[0 for _ in range(M+1)] for _ in range(N+1)]
chess_White=[[0 for _ in range(M+1)] for _ in range(N+1)]
for row in range(N):
    chess=sys.stdin.readline()
    for col in range(M):
        if chess[col]=="B":
            if (row+col) % 2 == 0: # 1,3번째 => 블랙 체스 O 화이트 체스 x
                chess_White[row+1][col+1]+=1
            else:
                chess_Black[row+1][col+1]+=1
        elif chess[col]=="W":
            if (row+col) % 2 == 0: # 1,3번째 
                chess_Black[row+1][col+1]+=1
            else:
                chess_White[row+1][col+1]+=1
        chess_Black[row+1][col+1]+=chess_Black[row+1][col]+chess_Black[row][col+1]-chess_Black[row][col]
        chess_White[row+1][col+1]+=chess_White[row+1][col]+chess_White[row][col+1]-chess_White[row][col]
black_min=N*M
white_min=N*M
for i in range(N-K+1):
    for j in range(M-K+1):
        x=chess_Black[i+K][j+K]-chess_Black[i][j+K]-chess_Black[i+K][j]+chess_Black[i][j]
        y=chess_White[i+K][j+K]-chess_White[i][j+K]-chess_White[i+K][j]+chess_White[i][j]
        if black_min>x:
            black_min=x
        if white_min>y:
            white_min=y

print(min(black_min,white_min))
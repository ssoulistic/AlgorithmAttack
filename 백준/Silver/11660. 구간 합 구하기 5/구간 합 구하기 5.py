import sys
N,M=map(int,sys.stdin.readline().split())
parsum=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    add=list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        parsum[i+1][j+1]=parsum[i+1][j]+parsum[i][j+1]-parsum[i][j]+add[j]
for _ in range(M):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    print(parsum[x2][y2]-parsum[x2][y1-1]-parsum[x1-1][y2]+parsum[x1-1][y1-1])

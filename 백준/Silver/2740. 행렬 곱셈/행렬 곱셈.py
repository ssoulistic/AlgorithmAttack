import sys
N,M=map(int,sys.stdin.readline().split())
A,B=[],[]
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))    
M,K=map(int,input().split())
for _ in range(M):
    B.append(list(map(int,sys.stdin.readline().split())))
C=[[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j]+=A[i][k]*B[k][j]
for c in C:
    print(*c)
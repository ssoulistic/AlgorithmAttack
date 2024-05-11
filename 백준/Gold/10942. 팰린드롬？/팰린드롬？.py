import sys
input=sys.stdin.readline
N=int(input())
seq=list(map(int,input().split()))
M=int(input())
dp=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i]=1

for j in range(N-1):
    if seq[j]==seq[j+1]:
        dp[j][j+1]=1

for length in range(3,N+1):
    for i in range(N-length+1):
        j=i+length-1
        if seq[i]==seq[j] and dp[i+1][j-1]:
            dp[i][j]=1
    
for _ in range(M):
    S,E=map(int,input().split())
    print(dp[S-1][E-1])
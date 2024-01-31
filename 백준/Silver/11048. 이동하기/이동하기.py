import sys
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[]
dp=[[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input().split())))
dp[0][0]=graph[0][0]
for l in range(M-1):
    dp[0][l+1]=dp[0][l]+graph[0][l+1]
for k in range(N-1):
    dp[k+1][0]=dp[k][0]+graph[k+1][0]
for i in range(N-1):
    for j in range(M-1):
        dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1],dp[i][j])+graph[i+1][j+1]
print(dp[N-1][M-1])
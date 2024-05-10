import sys
input=sys.stdin.readline

n,m=map(int,input().split())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,list(input().strip()))))
dp=[[0 for _ in range(m)] for _ in range(n)]
answer=0
for r1 in range(n):
    if matrix[r1][0]==1:
        dp[r1][0]=1
        answer=1
for c1 in range(m):
    if matrix[0][c1]==1:
        dp[0][c1]=1
        answer=1

for row in range(n-1):
    for col in range(m-1):
        if matrix[row+1][col+1]==1:
            dp[row+1][col+1]=min(dp[row+1][col],dp[row][col+1],dp[row][col])+1
            answer=max(answer,dp[row+1][col+1])

print(answer**2)
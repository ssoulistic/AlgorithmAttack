import sys
input=sys.stdin.readline
N,K=map(int,input().split())
dp=[[0 for _ in range(N+1)] for _ in range(K+1)]
for i in range(1,K+1):
    I,T = map(int,input().split()) #Importance,Time
    for t in range(1,N+1):
        if t>=T:
            dp[i][t]=max(dp[i-1][t-T]+I,dp[i-1][t])
        else:
            dp[i][t]=dp[i-1][t]
print(dp[-1][-1])
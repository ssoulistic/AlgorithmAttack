import sys
input=sys.stdin.readline
mod=10**9+3
N=int(input())
K=int(input())
if N<K*2:
    print(0)
else:
    dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        dp[i][1]=i
    for i in range(4,N+1):
        for j in range(2,i//2+1):
            dp[i][j]=dp[i-2][j-1]+dp[i-1][j]
    print(dp[N][K]%mod)
        

    
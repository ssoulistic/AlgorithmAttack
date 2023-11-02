T=int(input())
dp=[10**6//3 for _ in range(3*T+1)]
dp[0]=0
dp[1]=0
dp[2]=1
for i in range(1,T):
    dp[i*3]=min(dp[i]+1,dp[i*3])
    dp[i*2]=min(dp[i]+1,dp[i*2])
    dp[i+1]=min(dp[i]+1,dp[i+1])
print(dp[T])
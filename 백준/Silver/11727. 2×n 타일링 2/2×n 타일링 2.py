T=int(input())
dp=[0 for _ in range(1001)]
dp[0]=1
dp[1]=1
dp[2]=3
dp[3]=dp[2]+2*dp[1]
for i in range(T-1):
    dp[i+2]=dp[i+1]+2*dp[i]
print(dp[T] %10007)
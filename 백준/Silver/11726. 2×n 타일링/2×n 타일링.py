T=int(input())
dp=[1 for _ in range(1001)]
dp[1]=1
dp[2]=2
dp[3]=3
for i in range(T-1):
    dp[i+2]=dp[i+1]+dp[i]
print(dp[T]%10007)
T=int(input())
dp=[0 for _ in range(T+1)]
dp[1]=1 #1
dp[2]=2 #1+1 2
dp[3]=4 #1+1+1 1+2 2+1 3

dp=[0 for _ in range(12)]
def addmethod(n):
    dp[1]=1 #1
    dp[2]=2 #1+1 2
    dp[3]=4 #1+1+1 1+2 2+1 3
    if dp[n]==0:
        for i in range(1,n-2):
            dp[i+3]=dp[i+2]+dp[i+1]+dp[i]
    return dp[n]


for _ in range(T):
    print(addmethod(int(input())))
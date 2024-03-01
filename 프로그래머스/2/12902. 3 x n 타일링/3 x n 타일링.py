def solution(n):
    dp=[0 for _ in range(n+5)]
    dp[2]=3
    dp[4]=11
    for i in range(2,n+1,2):
        dp[i+4]=(3*dp[i+2]+2*sum(dp[i-j] for j in range(0,i,2))+2) % 1000000007
    return dp[n]
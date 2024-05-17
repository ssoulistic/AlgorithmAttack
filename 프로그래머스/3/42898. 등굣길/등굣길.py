def solution(m, n, puddles):
    graph=[[0 for _ in range(m)] for _ in range(n)]
    dp=[[0 for _ in range(m)] for _ in range(n)]
    dp[0][0]=1
    if puddles:
        for r,c in puddles:
            graph[c-1][r-1]=1
    for i in range(m):
        if graph[0][i]!=1:
            dp[0][i]=1
        else:
            break
    for j in range(n):
        if graph[j][0]!=1:
            dp[j][0]=1
        else:
            break
    for r in range(n-1):
        for c in range(m-1):
            if graph[r+1][c+1]!=1:
                dp[r+1][c+1]=(dp[r][c+1]+dp[r+1][c])%1000000007
    print(dp)
    return dp[n-1][m-1]%1000000007
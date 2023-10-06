n=int(input()) 
def stair(m):
    dp=[[0 for _ in range(10)] for _ in range(m)] #길이가 m인 계단수.dp[m-1][끝수] => 길이가 m-1인 숫자 x으로 끝나는 계단
    dp[0]=[0]+[1 for _ in range(9)]
    for i in range(1,m):
        for j in range(10):
            if j ==0:
                dp[i][j]=dp[i-1][j+1]
            elif j ==9:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
    return sum(dp[m-1])
print(stair(n)% 1000000000)
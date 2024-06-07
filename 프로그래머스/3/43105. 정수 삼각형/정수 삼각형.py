def solution(triangle):
    dp=[[0 for _ in range(i)] for i in range(1,len(triangle)+1)]
    dp[0][0]=triangle[0][0]
    for j in range(1,len(triangle)):
        for k in range(j+1):          
            if k==0:
                left=0
                right=dp[j-1][k]
            elif k==j:
                left=dp[j-1][k-1]
                right=0
            else:
                left=dp[j-1][k-1]
                right=dp[j-1][k]
            dp[j][k]=max(left,right)+triangle[j][k]
    return max(dp[-1])
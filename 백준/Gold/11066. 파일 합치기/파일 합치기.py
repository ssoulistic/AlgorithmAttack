import sys
input=sys.stdin.readline 
T=int(input())
for _ in range(T):
    K=int(input())
    file_sizes=list(map(int,input().split()))
    acc_fs=[0]
    for p in range(K):
        acc_fs.append(acc_fs[-1]+file_sizes[p])
    dp=[[float("inf")]*K for _ in range(K)]
    for j in range(K):
        dp[j][j]=0
    for length in range(1,K+1):
        for row in range(K-length):
            col=row+length
            for i in range(length):
                if dp[row][col]>dp[row+length-i][col]+dp[row][col-1-i]+acc_fs[col+1]-acc_fs[row]:
                    dp[row][col]=dp[row+length-i][col]+dp[row][col-1-i]+acc_fs[col+1]-acc_fs[row]
    print(dp[0][K-1])
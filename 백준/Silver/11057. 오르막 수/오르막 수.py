import sys
input=sys.stdin.readline
N=int(input())
case=[10-l for l in range(10)]
dp=[[0 for _ in range(10)] for _ in range(N)]
dp[0]=case
for k in range(1,N):
    for i in range(10):
        for j in range(i,10):
            dp[k][i]+=dp[k-1][j]
print(dp[N-1][0]% 10007)

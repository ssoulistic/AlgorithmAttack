import sys
input=sys.stdin.readline
N,M=map(int,input().split())
dp=[[0 for _ in range(M+1)] for _ in range(N+1)]
for idx in range(1,M+1):
    day,page=map(int,input().split())
    for max_day in range(N+1):
        if max_day>=day:
            dp[max_day][idx]=max(dp[max_day-day][idx-1]+page,dp[max_day][idx-1])
        else:
            dp[max_day][idx]=dp[max_day][idx-1]
print(dp[-1][-1])

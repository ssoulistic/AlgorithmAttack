import sys
input=sys.stdin.readline
N=int(input())
health=list(map(int,input().split()))
happiness=list(map(int,input().split()))

dp=[[0 for _ in range(N+1)] for _ in range(99+1)]
for idx in range(1,N+1):
    for max_health in range(100):
        if max_health-health[idx-1]>=0:
            dp[max_health][idx]=max(dp[max_health-health[idx-1]][idx-1]+happiness[idx-1],dp[max_health][idx-1])
        else:
            dp[max_health][idx]=dp[max_health][idx-1]
print(dp[-1][-1])   
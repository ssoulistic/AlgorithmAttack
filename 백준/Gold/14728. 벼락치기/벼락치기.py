import sys
input=sys.stdin.readline
N,T=map(int,input().split())
work=[]
dp=[[0 for _ in range(N+1)] for _ in range(T+1)]
for _ in range(N):
    K,S=map(int,input().split())
    work.append([K,S])
for idx in range(1,N+1):
    K,S=work[idx-1]
    for time in range(1,T+1):
        if time-K>=0:
            dp[time][idx]=max(dp[time-K][idx-1]+S,dp[time][idx-1])
        else:
            dp[time][idx]=dp[time][idx-1]
print(dp[-1][-1])
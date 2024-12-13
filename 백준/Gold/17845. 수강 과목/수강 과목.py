import sys
input=sys.stdin.readline
N,K=map(int,input().split())
dp=[0 for _ in range(N+1)]
for _ in range(1,K+1):
    I,T = map(int,input().split()) #Importance,Time
    for t in range(N,T-1,-1):
        now=dp[t-T]+I
        if dp[t]<now:
            dp[t]=now
print(dp[-1])
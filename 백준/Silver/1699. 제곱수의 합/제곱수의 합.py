import sys
input=sys.stdin.readline
N=int(input())
end=int(N**0.5)+1
dp=[l for l in range(N+1)]
for i in range(1,end):
    dp[i**2]=1

for p in range(1,N+1):
    for q in range(1,int(p**0.5)+1):
        if p+q**2<=N:
            dp[p+q**2]=min(dp[p+q**2],dp[p]+1)
print(dp[N])
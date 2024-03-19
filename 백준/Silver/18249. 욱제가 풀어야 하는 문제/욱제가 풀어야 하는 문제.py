import sys
input=sys.stdin.readline
T=int(input())

lists=[]
def cross(n):
    if dp[n]!=0:
        return dp[n]
    for i in range(2,n+1):
        dp[i]=(dp[i-1]+dp[i-2]) % (10**9+7)
    return dp[n]

for _ in range(T):
    N=int(input())
    lists.append(N-1)
maximum=max(lists)
dp=[0 for _ in range(maximum+1)]
dp[0]=1
if maximum>=1:
    dp[1]=2
cross(maximum)
for l in lists:
    print(dp[l])
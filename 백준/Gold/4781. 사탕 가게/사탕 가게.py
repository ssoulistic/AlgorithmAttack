import sys
input=sys.stdin.readline
n=1
while n!=0:
    n,m=input().split()
    n=int(n)
    m=int(float(m)*100+0.1)
    dp=[0 for _ in range(m+1)]
    for _ in range(n):
        c,p=input().split()
        c=int(c)
        p=int(float(p)*100+0.1)
        for j in range(p,m+1):
            dp[j]=max(dp[j-p]+c,dp[j])
    if n!=0:
        print(dp[-1])
import sys
input=sys.stdin.readline

N=int(input())
seq=list(map(int,input().split()))
dp=[[1,[seq[k]]] for k in range(N)]
for i in range(N):
    for j in range(i):
        if seq[j]<seq[i]:
            if dp[i][0]<dp[j][0]+1:
                dp[i][0]=dp[j][0]+1
                dp[i][1]=dp[j][1]+[seq[i]]
maxi=0
for l in range(N):
    if dp[maxi][0]<dp[l][0]:
        maxi=l
print(dp[maxi][0])
print(*dp[maxi][1])
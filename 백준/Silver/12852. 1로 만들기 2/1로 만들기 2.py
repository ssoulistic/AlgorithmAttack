import sys
input=sys.stdin.readline
from collections import deque
N=int(input())
# 이전 경로, 지금까지 거리.
dp=[[False,2*N] for _ in range(N+1)]
dp[N]=[N,0]
que=deque()
que.append(N)
while que:
    next=que.popleft()
    if next==1:
        break
    if next % 3 ==0:
        if dp[next//3][1]>dp[next][1]:
            dp[next//3]=[next,dp[next][1]+1]
            que.append(next//3)
    if next % 2==0:
        if dp[next//2][1]>dp[next][1]:
            dp[next//2]=[next,dp[next][1]+1]
            que.append(next//2)
    if next-1>=1:
        if dp[next-1][1]>dp[next][1]:
            dp[next-1]=[next,dp[next][1]+1]
            que.append(next-1)
print(dp[1][1])

answer=[]
now=1
answer.append(1)
while now!=N:
    now=dp[now][0]
    answer.append(now)
print(*answer[::-1])
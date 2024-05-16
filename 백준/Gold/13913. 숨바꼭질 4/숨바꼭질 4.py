import sys
input=sys.stdin.readline
from collections import deque
N,K=map(int,input().split())
dp=[[1e6,i] for i in range(100001)]

dp[N][0]=0
queue=deque()
queue.append([N,0])
while queue and dp[K][1]==K:
    next,time=queue.popleft()
    for k in [lambda x: x+1, lambda x: x-1, lambda x: x*2]:
        next_num=k(next)
        if 0<=next_num<100001 and dp[next_num][0]>time+1:
            dp[next_num][0]=time+1
            dp[next_num][1]=next
            queue.append([next_num,time+1])
print(dp[K][0])

answer=[K]
queue2=deque()
queue2.append(dp[K][1])
while queue2:
    back=queue2.popleft()
    if answer[-1]!=back:
        answer.append(back)
        queue2.append(dp[back][1])
print(*answer[::-1])
    
    
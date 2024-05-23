import sys
input=sys.stdin.readline
T=int(input())
from collections import deque
for _ in range(T):
    N,K=map(int,input().split())
    build_time=list(map(int,input().split()))
    graph=[[] for _ in range(N)]
    indegree=[0 for _ in range(N)]
    dp=[0]*N
    for _ in range(K):
        X,Y=map(int,input().split())
        graph[X-1].append(Y-1)
        indegree[Y-1]+=1
    W=int(input())
    queue=deque()
    for i in range(N):
        if indegree[i]==0:
            queue.append(i)
            dp[i]=build_time[i]

    while queue:
        next=queue.popleft()
        for next_build in graph[next]:
            indegree[next_build]-=1
            dp[next_build]=max(dp[next_build],dp[next]+build_time[next_build])
            if indegree[next_build]==0:
                queue.append(next_build)
    print(dp[W-1])
                
    
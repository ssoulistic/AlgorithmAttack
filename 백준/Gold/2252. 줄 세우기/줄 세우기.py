import sys
input=sys.stdin.readline
from collections import deque
N,M=map(int,input().split())
indegree=[0]*N
graph=[[] for _ in range(N)]
for _ in range(M):
    A,B=map(int,input().split())
    graph[A-1].append(B-1)
    indegree[B-1]+=1

queue=deque()
for i in range(N):
    if indegree[i]==0:
        queue.append(i)

answer=[]
while queue:
    v=queue.popleft()
    answer.append(v+1)
    for next in graph[v]:
        indegree[next]-=1
        if indegree[next]==0:
            queue.append(next)
print(*answer)
import sys
input=sys.stdin.readline
from collections import deque
N=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
root=[0 for _ in range(N+1)]
que=deque()
que.append(1)
while que:
    next=que.popleft()
    for x in graph[next]:
        if not root[x]:
            root[x]=next
            que.append(x)
for r in root[2:]:
    print(r)
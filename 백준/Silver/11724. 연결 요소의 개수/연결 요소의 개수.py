from collections import deque
import sys
N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
que=deque()
for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(x):
    if not visited[x]:
        visited[x]=True
        que.append(x)
        while que:
            next=que.popleft()
            for g in graph[next]:
                if not visited[g]:
                    visited[g]=True
                    que.append(g)
        return True
    else:
        return False

count=0
for i in range(1,N+1):
    if bfs(i):
        count+=1
print(count)
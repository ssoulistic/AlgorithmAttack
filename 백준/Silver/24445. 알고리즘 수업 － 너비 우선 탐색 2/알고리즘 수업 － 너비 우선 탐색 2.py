import sys
from collections import deque
N,M,R=map(int,sys.stdin.readline().split())
visited=[0 for _ in range(N+1)]
que=deque()
count=1
def bfs(graph,start):
    global count
    visited[start]=count
    que.append(start)
    while que:
        u=que.popleft()
        for v in sorted(graph[u],reverse=True):
            if not visited[v]:
                count+=1
                visited[v]=count
                que.append(v)
gp=[[] for _ in range(N+1)]
for _ in range(M):
    p,q=map(int,sys.stdin.readline().split())
    gp[p].append(q)
    gp[q].append(p)

bfs(gp,R)
for l in visited[1:]:
    print(l)
import sys
input=sys.stdin.readline
from collections import deque
N,K=map(int,input().split())
maximum=max(N,K)
visited=[0 for _ in range(2*maximum+1)]

def bfs(coord):
    visited[coord]=1
    que=deque()
    que.append(coord)
    while que:
        next=que.popleft()
        if next==K:
            return visited[K]
        for i in range(3):
            if i==0:
                nx=next-1
            elif i==1:
                nx=next+1
            elif i==2:
                nx=next*2
            if 0<=nx<=2*maximum:
                if visited[nx]>visited[next]+1 or visited[nx]==0:
                    visited[nx]=visited[next]+1
                    que.append(nx)
    return 
print(bfs(N)-1)
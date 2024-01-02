from collections import deque
import sys
N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(100)]
visited=[0 for _ in range(100)]
for _ in range(N+M):
    start,end=map(int,sys.stdin.readline().split())
    graph[start-1].append(end-1)
def bfs(n):
    if n==99:
        return
    if visited[n]:
        return
    que=deque()
    que.append(n)
    visited[n]=0
    while que:
        next=que.popleft()
        if graph[next]:
            visited[graph[next][0]]=visited[next]
            next=graph[next][0]
        for dice in range(1,7):
            if next+dice<100 and not visited[next+dice]:
                visited[next+dice]=visited[next]+1
                que.append(next+dice)
    return
bfs(0)
print(visited[99])
    

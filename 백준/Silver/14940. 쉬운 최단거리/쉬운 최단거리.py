from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())
graph=[]

visited=[[0 for _ in range(m)] for _ in range(n)]
search=[[-1,0],[1,0],[0,-1],[0,1]]
que=deque()
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            visited[i][j]=-1
        elif graph[i][j]==2:
            begin=[j,i]

def bfs(start):
    visited[start[1]][start[0]]=0
    que.append([start[0],start[1]])
    
    while que:
        node=que.popleft()
        for s in search:
            x1=node[0]+s[0]
            y1=node[1]+s[1]
            if 0<=x1<=m-1 and 0<=y1<=n-1 and visited[y1][x1]==-1:
                visited[y1][x1]=visited[node[1]][node[0]]+1
                que.append([x1,y1])

bfs(begin)
for v in visited:
    print(*v)
from collections import deque
N=int(input())
v1=[[False for _ in range(N)] for _ in range(N)]
v2=[[False for _ in range(N)] for _ in range(N)]
search=[[0,1],[0,-1],[1,0],[-1,0]]
graph=[]
domain1,domain2=0,0
for _ in range(N):
    graph.append(input())

def bfs(coord,rgblind,visited):
    x,y=coord
    color=["R","G"]
    if visited[y][x]:
        return False
    if not rgblind:
        color=[graph[y][x]]
    else:
        if graph[y][x] not in color:
            color=["B"]
    que=deque()
    que.append([x,y])
    while que:
        next=que.popleft()
        for s in search:
            nx=next[0]+s[0]
            ny=next[1]+s[1]
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and graph[ny][nx] in color:
                visited[ny][nx]=True
                que.append([nx,ny])
    return True

for i in range(N):
    for j in range(N):
        if bfs([i,j],False,v1):
            domain1+=1
        if bfs([i,j],True,v2):
            domain2+=1
print(domain1,domain2)
from collections import deque
N,M=map(int,input().split())
graph=[[0 for _ in range(M)] for _ in range(N)]
visited=[[False for _ in range(M)] for _ in range(N)]
search=[[1,0],[-1,0],[0,1],[0,-1]]
que=deque()

for i in range(N):
    line=input()
    for j in range(M):
        if line[j]=="0":
            graph[i][j]=1
            visited[i][j]=True
def bfs(x,y):
    
    if not visited[y][x]:
        visited[y][x]=1
        que.append([x,y])
        while que:
            node=que.popleft()
            for s in search:
                x1=node[0]+s[0]
                y1=node[1]+s[1]
                if 0<=x1<=M-1 and 0<=y1<=N-1 and not visited[y1][x1]:
                    visited[y1][x1]=visited[node[1]][node[0]]+1
                    que.append([x1,y1])

    return visited
                    
print(bfs(0,0)[N-1][M-1])
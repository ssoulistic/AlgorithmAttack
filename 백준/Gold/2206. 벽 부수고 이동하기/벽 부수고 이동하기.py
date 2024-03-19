import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().strip().split())
walls=[]
graph=[]
for row in range(N):
    line=list(map(int,list(input().strip())))
    for col in range(M):
        if line[col]==1:
            walls.append([row,col])
    graph.append(line)

def bfs(start):
    visited=[[False for _ in range(M)] for _ in range(N)]
    r,c=start
    visited[r][c]=1
    que=deque()
    que.append([r,c])
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    while que:
        ri,ci=que.popleft()
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<N and 0<=nc<M:
                if graph[nr][nc]==0:
                    if not visited[nr][nc] or visited[nr][nc]>visited[ri][ci]+1:                            
                        visited[nr][nc]=visited[ri][ci]+1
                        que.append([nr,nc])
                elif graph[nr][nc]==1:
                    if visited[nr][nc]:
                        visited[nr][nc]=min(visited[nr][nc],visited[ri][ci]+1)
                    else:
                        visited[nr][nc]=visited[ri][ci]+1
    return visited

normal_path=bfs([0,0])
reverse_path=bfs([N-1,M-1])
normal_distance=normal_path[N-1][M-1]

if walls:
    answer=N*M+1
    for wr,wc in walls:
        if normal_path[wr][wc] and reverse_path[wr][wc]:
            if answer>normal_path[wr][wc]+reverse_path[wr][wc]-1:
                answer=normal_path[wr][wc]+reverse_path[wr][wc]-1         
else:
    answer=normal_distance
if answer==N*M+1:
    print(-1)
else:
    print(answer)
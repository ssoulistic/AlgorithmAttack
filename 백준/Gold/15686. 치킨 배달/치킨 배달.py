import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque
N,M=map(int,input().split())
city=[]
chicken=[]
home=[]
for r in range(N):
    line=list(map(int,input().split()))
    for c in range(N):
        if line[c]==2:
            chicken.append([r,c])
        elif line[c]==1:
            home.append([r,c])
    city.append(line)

def bfs(start):
    ri,ci=start
    visited[ri][ci]=1
    que=deque()
    que.append([ri,ci])
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    while que:
        rii,cii=que.popleft()
        for dr,dc in search:
            nr=rii+dr
            nc=cii+dc
            if 0<=nr<N and 0<=nc<N:
                if visited[nr][nc]>visited[rii][cii]+1:
                    visited[nr][nc]=visited[rii][cii]+1
                    que.append([nr,nc])
                elif visited[nr][nc]==0:
                    visited[nr][nc]=visited[rii][cii]+1
                    que.append([nr,nc])
answer=N**N
for combo in combinations(chicken,M):
    visited=[[0 for _ in range(N)] for _ in range(N)]
    for case in combo:
        bfs(case)
    chicken_distance=0
    for hr,hc in home:
        chicken_distance+=(visited[hr][hc]-1)
    if answer>chicken_distance:
        answer=chicken_distance
print(answer)
    

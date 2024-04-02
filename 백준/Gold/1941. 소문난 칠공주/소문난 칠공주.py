import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque
def bfs(start):
    count=1
    r,c=start
    visited[r][c]=True
    que=deque()
    que.append([r,c])
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    while que:
        ri,ci=que.popleft()
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc]:
                visited[nr][nc]=True
                count+=1
                que.append([nr,nc])
    if count==7:
        return True
    else:
        return False
graph=[]
for _ in range(5):
    graph.append(list(input().strip()))   
answer=0
for combo in combinations([[i,j] for i in range(5) for j in range(5)],7):
    visited=[[True for _ in range(5)] for _ in range(5)]
    som=0
    for ri,ci in combo:
        if graph[ri][ci]=="S":
            som+=1
        visited[ri][ci]=False
    
    if som>=4 and bfs(combo[0]):
        answer+=1
print(answer)
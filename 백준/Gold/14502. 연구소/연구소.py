import sys
input=sys.stdin.readline
from itertools import combinations
import copy
N,M=map(int,input().split()) # N 세로 M 가로
viruses=[]
blank=[]
graph=[]
for r in range(N):
    line=list(map(int,input().split()))
    for c in range(M):
        if line[c]==2:
            viruses.append([r,c])
        elif line[c]==0:
            blank.append([r,c])
    graph.append(line)
    

def bfs(graph2,walls,virus):
    new_map=copy.deepcopy(graph2)
    visited=[[False for _ in range(M)] for _ in range(N)]
    # 1. 벽 치기.
    for wr,wc in walls:
        new_map[wr][wc]=1
    # 2. 바이러스 확산
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    for vr,vc in virus:
        visited[vr][vc]=True
    que=virus[:]
    while que:
        nr,nc=que.pop(0)
        for dr,dc in search:
            rr=nr+dr
            cc=nc+dc
            if 0<=rr<N and 0<=cc<M:
                if not visited[rr][cc] and new_map[rr][cc]==0:
                    que.append([rr,cc])
                visited[rr][cc]=True
    # 3. 0 세기
    count=0
    for r in range(N):
        for c in range(M):
            if visited[r][c]==False and new_map[r][c]==0:
                count+=1
    return count

answer=0
for combo in combinations(blank,3):
    safe=bfs(graph,combo,viruses)
    if answer<safe:
        answer=safe
print(answer)
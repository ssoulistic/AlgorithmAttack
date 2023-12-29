import sys
from collections import deque
H,M,N=map(int,sys.stdin.readline().strip().split())
total=H*M*N
tmt=[]
seed=[]
answer=0
for k in range(N):
    floor=[]
    for j in range(M):
        line=list(map(int,sys.stdin.readline().strip().split()))
        for i in range(H):
            if line[i]==1:
                seed.append([i,j,k])
            elif line[i]==-1:
                total-=1
        floor.append(line)
    tmt.append(floor)
total-=len(seed)
search=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]

def growth(start):
    que=deque()
    que.append(start)
    while que:
        next=que.popleft()
        for s in search:
            nx=next[0]+s[0]
            ny=next[1]+s[1]
            nz=next[2]+s[2]
            if 0<=nx<H and 0<=ny<M and 0<=nz<N and tmt[nz][ny][nx]!=-1:
                if tmt[nz][ny][nx]>tmt[next[2]][next[1]][next[0]]+1 or tmt[nz][ny][nx]==0:
                    tmt[nz][ny][nx]=tmt[next[2]][next[1]][next[0]]+1
                    que.append([nx,ny,nz])
                
if total:
    for sd in seed:
        growth(sd)
    for k in range(N):
        for j in range(M):
            for i in range(H):
                if answer==-1:
                    break
                elif tmt[k][j][i]==0:
                    answer=-1
                elif answer<tmt[k][j][i]:
                    answer=tmt[k][j][i]-1
            
print(answer)
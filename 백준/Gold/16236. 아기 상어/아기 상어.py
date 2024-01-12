import sys
input=sys.stdin.readline
from collections import deque

T=int(input())
fish_map=[]
for row in range(T):
    line=list(map(int,input().split()))
    for col in range(T):
        if line[col]==9:
            start=[col,row]
    fish_map.append(line)
fish_map[start[1]][start[0]]=0

# 가장 가까운 녀석의 냄새를 맡음 => 여러개면 가장 상단,위쪽의 녀석 우선 => 이동하여 먹음(크기 변화 체크) / 반복
search=[[0,-1],[-1,0],[1,0],[0,1]]
def smell(shark_coord,shark_size):
    visited=[[0 for _ in range(T)] for _ in range(T)]
    x,y=shark_coord
    visited[y][x]=1
    que=deque()
    que.append([x,y])
    target=[T**2,T,T]
    while que:
        xi,yi=que.popleft()
        for dx,dy in search:
            nx=xi+dx
            ny=yi+dy
            if 0<=nx<T and 0<=ny<T and not visited[ny][nx]:
                visited[ny][nx]=visited[yi][xi]+1
                if fish_map[ny][nx]<=shark_size:
                    que.append([nx,ny])
                if fish_map[ny][nx]!=0 and fish_map[ny][nx]<shark_size:
                    target=min(target,[visited[ny][nx],ny,nx])
    return target   

level=2
eaten=0
answer=0
while True:
    distance,ky,kx = smell(start,level)
    if kx==T:
        break
    fish_map[ky][kx]=0
    eaten+=1
    answer+=distance-1
    start=[kx,ky]
    if level<=eaten:
        level+=1
        eaten=0
print(answer)

import sys
from collections import deque
N,M=map(int,sys.stdin.readline().strip().split())
campus=[]
answer=0
for j in range(N):
    temp=[]
    line=sys.stdin.readline().strip()
    for i in range(M):
        if line[i]=="I":
            doyeon=[i,j]
            temp.append("O")
        else:
            temp.append(line[i])
    campus.append(temp)
    

search=[[1,0],[-1,0],[0,1],[0,-1]]
que=deque()
def bfs(coord):
    global answer
    x,y=coord
    if campus[y][x]=="O":
        que.append([x,y])
        campus[y][x]="X"
        while que:
            next=que.popleft()
            for s in search:
                nx=next[0]+s[0]
                ny=next[1]+s[1]
                if 0<=nx<M and 0<=ny<N and campus[ny][nx]!="X":
                    if campus[ny][nx]=="P":
                        answer+=1
                    campus[ny][nx]="X"
                    que.append([nx,ny])
bfs(doyeon)    
if answer:
    print(answer)
else:
    print("TT")                
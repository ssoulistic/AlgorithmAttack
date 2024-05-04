import sys
input=sys.stdin.readline
N,M=map(int,input().split())
from collections import deque
graph=[]
answer=[[0 for _ in range(M)] for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]
dic={}
group=1
search=[[0,1],[1,0],[0,-1],[-1,0]]


for _ in range(N):
    graph.append(list(input().strip()))

def zero_bfs(r,c):
    global answer
    global group
    if visited[r][c]:
        return visited[r][c]
    if dic.get(group):
        group+=1
    visited[r][c]=group
    queue=deque([[r,c]])
    count=1
    while queue:
        ri,ci=queue.popleft()
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and graph[nr][nc]=="0":
                    count+=1
                    visited[nr][nc]=group
                    queue.append([nr,nc])
    dic[group]=count
    return group

for row in range(N):
    for col in range(M):
        if graph[row][col]=="1":
            answer[row][col]+=1
            atmo=set()
            for drr,dcc in search:
                rr=row+drr
                cc=col+dcc
                if 0<=rr<N and 0<=cc<M and graph[rr][cc]=="0":
                    if visited[rr][cc]:
                        atmo.add(visited[rr][cc])
                    else:
                        atmo.add(zero_bfs(rr,cc))
            for at in atmo:
                answer[row][col]+=dic[at]
        elif graph[row][col]=="0":
            zero_bfs(row,col)

for row in range(N):
    for col in range(M):
        print(answer[row][col]%10,end="")
    print()
    
from collections import deque
M,N=map(int,input().split())# M가로 N 세로
# 0 이 없을때 => 최대
# 0 이 있으면 -1
graph=[]
que=deque()
search=[[1,0],[-1,0],[0,1],[0,-1]]
begin=[]
for i in range(N):
    graph.append(list(map(int,input().split())))
for p in range(N):
    for q in range(M):
        if graph[p][q]==1:
            begin.append([q,p])
def bfs(starts):
    for x,y in starts:
        que.append([x,y])
    while que:
        next=que.popleft()
        for s in search:
            x1=next[0]+s[0]
            y1=next[1]+s[1]
            if 0<=x1<=M-1 and 0<=y1<=N-1 and graph[y1][x1]==0:
                graph[y1][x1]=graph[next[1]][next[0]]+1
                que.append([x1,y1])
    return graph
result=bfs(begin)
answer=0
for a in result:
    if 0 in a:
        answer=0
        break
    if answer<max(a):
        answer=max(a)
print(answer-1)
from collections import deque
N=int(input())
que=deque()
search=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
def bfs(graph,x,y):
    graph[y][x]=1
    que.append([x,y])
    while que:
        next=que.popleft()
        for s in search:
            xx=next[0]+s[0]
            yy=next[1]+s[1]
            if 0<=xx<=l-1 and 0<=yy<=l-1 and not graph[yy][xx]:
                graph[yy][xx]=graph[next[1]][next[0]]+1
                que.append([xx,yy])
    return graph
for _ in range(N):
    l=int(input()) # 변의 길이
    mp=[[False for _ in range(l)] for _ in range(l)]
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    print(bfs(mp,x1,y1)[y2][x2]-1)
    
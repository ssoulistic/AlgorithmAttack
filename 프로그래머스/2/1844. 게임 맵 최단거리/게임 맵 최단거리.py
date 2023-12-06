from collections import deque
def solution(maps):
    visited=[[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for p in range(len(maps)):
        for q in range(len(maps[0])):
            if maps[p][q]==1:
                visited[p][q]=0
            else:
                visited[p][q]=1
    
    def bfs(x,y):
        que=deque()
        search=[[0,1],[0,-1],[1,0],[-1,0]]
        if visited[y][x]==0:
            visited[y][x]=1
            que.append([x,y])
        while que:
            next=que.popleft()
            for s in search:
                x1=next[0]+s[0]
                y1=next[1]+s[1]
                if 0<=x1<len(maps[0]) and 0<=y1<len(maps) and visited[y1][x1]==0:
                    visited[y1][x1]=visited[next[1]][next[0]]+1
                    que.append([x1,y1])
    bfs(0,0)
    answer=visited[len(maps)-1][len(maps[0])-1]
    if answer==0:
        answer=-1
    
    return answer